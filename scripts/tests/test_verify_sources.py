# ABOUTME: Unit tests for file-backed source support in verify-sources.py (schema,
# ABOUTME: local-only checks, cross-check) + the data-file-source exemption in check-citation-links.py.
import hashlib
import subprocess


def entry(**kw):
    base = {"id": "e1", "authority": "internal", "title": "T"}
    base.update(kw)
    return base


class TestValidateSchema:
    def test_url_entry_with_quote_passes(self, vs):
        assert vs.validate_schema([entry(url="https://x.com/a", quote="q")]) == []

    def test_both_url_and_file_fails(self, vs):
        probs = vs.validate_schema([entry(url="https://x.com/a", file="d/x.json", quote="q")])
        assert any("exactly one of" in p for p in probs)

    def test_neither_url_nor_file_fails(self, vs):
        probs = vs.validate_schema([entry()])
        assert any("exactly one of" in p for p in probs)

    def test_plain_file_entry_needs_no_quote(self, vs):
        assert vs.validate_schema([entry(file="docs/x.md")]) == []

    def test_local_only_requires_sha256_and_reason(self, vs):
        probs = vs.validate_schema([entry(file="d/x.json", verify="local-only")])
        assert any("REQUIRES sha256" in p for p in probs)
        assert any("REQUIRES a reason" in p for p in probs)

    def test_unknown_verify_mode_on_file_fails(self, vs):
        probs = vs.validate_schema([entry(file="d/x.json", verify="link-only")])
        assert any("unknown verify mode" in p for p in probs)

    def test_absolute_file_path_fails(self, vs):
        probs = vs.validate_schema([entry(file="/etc/passwd")])
        assert any("repo-relative path" in p for p in probs)

    def test_dotdot_file_path_fails(self, vs):
        probs = vs.validate_schema([entry(file="../../etc/passwd")])
        assert any("repo-relative path" in p for p in probs)


class TestCheckFileEntry:
    def test_promoted_missing_file_fails(self, vs, tmp_path):
        probs, warns = vs.check_file_entry(
            entry(file="gone.md"), repo_root=tmp_path, tracked=lambda p, r: True)
        assert any("MISSING" in p for p in probs) and warns == []

    def test_promoted_untracked_fails(self, vs, tmp_path):
        (tmp_path / "a.md").write_text("x")
        probs, _ = vs.check_file_entry(
            entry(file="a.md"), repo_root=tmp_path, tracked=lambda p, r: False)
        assert any("not git-tracked" in p for p in probs)

    def test_promoted_tracked_ok(self, vs, tmp_path):
        (tmp_path / "a.md").write_text("x")
        probs, warns = vs.check_file_entry(
            entry(file="a.md"), repo_root=tmp_path, tracked=lambda p, r: True)
        assert probs == [] and warns == []

    def test_local_only_absent_warns_not_fails(self, vs, tmp_path):
        probs, warns = vs.check_file_entry(
            entry(file="gone.bin", verify="local-only", sha256="00", reason="heavy"),
            repo_root=tmp_path)
        assert probs == [] and any("ABSENT" in w for w in warns)

    def test_local_only_sha_match_ok(self, vs, tmp_path):
        p = tmp_path / "a.bin"
        p.write_bytes(b"data")
        good = hashlib.sha256(b"data").hexdigest()
        probs, warns = vs.check_file_entry(
            entry(file="a.bin", verify="local-only", sha256=good, reason="heavy"),
            repo_root=tmp_path)
        assert probs == [] and warns == []

    def test_local_only_sha_mismatch_fails(self, vs, tmp_path):
        p = tmp_path / "a.bin"
        p.write_bytes(b"data")
        probs, _ = vs.check_file_entry(
            entry(file="a.bin", verify="local-only", sha256="deadbeef", reason="heavy"),
            repo_root=tmp_path)
        assert any("MISMATCH" in p for p in probs)


class TestIsGitTracked:
    def test_tracked_and_untracked_in_a_real_repo(self, vs, tmp_path):
        subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
        tracked = tmp_path / "tracked.md"
        tracked.write_text("x")
        subprocess.run(["git", "add", "tracked.md"], cwd=tmp_path, check=True)
        untracked = tmp_path / "untracked.md"
        untracked.write_text("y")
        assert vs.is_git_tracked(tracked, tmp_path) is True
        assert vs.is_git_tracked(untracked, tmp_path) is False


class TestCrossCheck:
    def test_unregistered_file_marker_fails(self, vs):
        probs, _ = vs.cross_check([], ["mystery"], [entry(file="a.md")])
        assert any('UNREGISTERED file source: data-file-source="mystery"' in p for p in probs)

    def test_stale_file_entry_warns(self, vs):
        _, warns = vs.cross_check([], [], [entry(file="a.md")])
        assert any("'e1' is not cited" in w for w in warns)

    def test_registered_marker_clean(self, vs):
        probs, warns = vs.cross_check([], ["e1"], [entry(file="a.md")])
        assert probs == [] and warns == []


class TestDeckFileSourceIds:
    def test_extracts_unique_ids_in_order(self, vs):
        html = ('<span data-file-source="a">x</span>'
                '<span data-file-source="b">y</span>'
                '<span data-file-source="a">x</span>')
        assert vs.deck_file_source_ids(html) == ["a", "b"]


class TestUnclickableExemption:
    FOOTER = '<small class="sources">Sources : {inner}</small>'

    def test_file_source_line_without_anchor_passes(self, ccl):
        html = self.FOOTER.format(
            inner='[D1] <span data-file-source="probe-log">probe_log.jsonl</span>')
        assert ccl.unclickable_sources(html) == []

    def test_plain_text_source_line_still_fails(self, ccl):
        html = self.FOOTER.format(inner="[1] some report, trust me")
        assert any("NO clickable link" in reason for reason, _ in ccl.unclickable_sources(html))
