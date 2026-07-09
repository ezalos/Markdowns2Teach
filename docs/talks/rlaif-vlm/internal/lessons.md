# Lessons — Hackathon-07-01 (RLAIF VLM DPO)

Reusable rules learned while building the harness + Phase-1 training body. Read at session start.

## Research / planning
- **Verify agent-provided version numbers against the real index.** The stack-research agent gave
  `torch==2.12.1 cu128`, which does not exist (cu128 tops out at 2.11.0). Always `curl` the actual
  PyPI/torch index and pin what's really there; prefer floors + let uv resolve over invented exacts.
- **Trust code over changelogs.** The trackio-research agent said `Table(columns=, data=)` is
  supported; the installed 0.29 source has it stubbed (`# TODO ... don't do anything`). When a lib
  call misbehaves, read the installed source, not the docs.

## Git
- **Never `git add -A` here.** It swept Louis's untracked scaffolding (DESIGN.md, main.py, .envrc)
  into a commit unintentionally. Stage explicit paths.

## smic environment
- **Home disk is tight (~13 G free); `/dev/shm` (63 G, RAM) is writable, `/srv/fastdata` is not.**
  Point `HF_HOME=/dev/shm/$USER/hf` for model/dataset cache. Don't `load_dataset(split="train")` on
  RLAIF-V (full multi-GB download) — **stream + materialize a small slice** instead.
- **tmux windows need an explicit command** (login zsh exits under `TERM=dumb` over non-interactive
  ssh and kills the server). Run the command directly + end with `exec bash --norc`.
- **`python src/x.py` doesn't put repo root on sys.path** → set `PYTHONPATH=$PWD` (in remote_launch.sh)
  so `import data` / `import src` resolve. Same fix as pytest's `pythonpath = ["."]`.

## Trackio (0.29)
- **Build tables with `Table(dataframe=pd.DataFrame(...))`, never `columns=/data=`** — the latter yields
  integer column keys → orjson "Dict key must be str" crash in the background sender.
- **Own the run: `trackio.init()` yourself + `report_to=[]` + a scalar-forwarding callback.** The
  Trainer's `report_to=["trackio"]` integration (a) auto-deploys a HF Space (hangs on a token prompt —
  `TrainingArguments.trackio_space_id` defaults to `"trackio"`), and (b) races on `configs.run_id`.
- **A crashed run corrupts the SQLite DB** → later runs fail with `configs.run_id NOT NULL`. Wipe
  `untracked_files/trackio/*` after a failed run.

## VLM DPO (TRL 1.7 / transformers 4.57)
- Force `.convert("RGB")` on every RLAIF-V image (#1 crash). `max_length=None` (truncation cuts image
  tokens). Pass `processing_class=<AutoProcessor>`, `ref_model=None`, `attn_implementation="sdpa"`.
- 500M validates plumbing, not gains: reward margin stayed flat, probe outputs stable over 250 steps.
  Real delta is a Phase-2 (3B) outcome — one config line on the proven harness.
- **Freezing a VLM's vision encoder needs TWO things:** `requires_grad=False` on the base weights AND
  `exclude_modules=".*vision.*"` on the LoRA config — else `target_modules=[q/k/v/o_proj]` matches the
  vision tower's attention and LoRA adapts it anyway. Caught by `make verify` (72 vision LoRA params
  trainable). Verify structural freeze, not just the base-weight loop.

## Verifying training correctness (see `make verify` + tasks/rl-verification-checklist.md)
- The DPO overfit test: loss must start at **exactly ln2 = 0.6931** (proves policy==ref, β/sign
  correct), then crater to ~0 on 2 memorized pairs with `lora_dropout=0` + constant LR; accuracy -> 1.0,
  margin -> large. If loss stays 0.693 -> nothing is training. Codified as an assertion in `verify_wiring.py`.
- An overfit that passes while the real run stays flat = the model/data is the limit, not the code.

## RLAIF / Phase 4b
- **Standalone generation scripts must `model.to("cuda")`** — `build_model_and_processor` loads on CPU;
  only the HF Trainer moves it to GPU. A generate script without it runs on CPU (100x slower). Caught via GPU=0MiB.
- **Free OpenRouter vision models exist** (`nvidia/nemotron-3-nano-omni-...:free`) and judge acceptably —
  default to free for unattended/budget-limited runs ($0). Paid opt-in only.
- **3B trials are ~11GB regardless of vision-token trimming** (weights dominate) -> concurrency **2**, not 3, on 24GB.
  My overnight batch OOM'd 4/6 jobs at concurrency 3. Size 3B parallelism by weights, not activations.
- Config refs that assume RLAIF-V (`cfg["data"]["train_size"]`) break for the local-preferences path -> use `.get`.
- **3B needs concurrency 1 for reliability.** Even 2 concurrent 3B trials (~11.4GB each = 22.8GB) OOM at
  peaks on a 24GB card. My redo at conc 2 OOM'd 2/4 jobs. Run 3B experiments solo; parallelism is a 500M luxury.
- **RLAIF iteration over-optimizes a weak judge.** Round 1 (from base) helped 56%; round 2 (on-policy from
  the round-1 model) DROPPED to 37.5% vs base — reward hacking (Gao et al.). The free judge's noise
  dominated once the model shrank toward its taste. Judge quality is the RLAIF bottleneck, not the loop.
- **Eval-slice confound:** load_datasets takes eval rows RIGHT AFTER train_size, so changing train_size
  silently changes the eval distribution (RLAIF-V is unshuffled blocks of source datasets). Cross-run
  eval-acc comparisons were contaminated. Fix: standalone eval on a fixed untouched slice (src/eval_pref.py,
  offset 20000). Lesson: pin the eval set ONCE, independently of all training knobs.
- **pgrep -f self/ghost-matching (2nd incident):** the detached `tmux new-session` client keeps the full
  launch string in its cmdline; `pgrep -f "train_dpo.py --config X"` matched it forever and hung the
  postrun watcher 45 min. Always anchor patterns on the interpreter path: `pgrep -f "bin/python3 src/x.py"`.
- **Fixed-slice contamination (caught 08:20 final morning):** the "never-trained" eval slice @20000 was chosen
  when max train_size was 16k; the 24k run then trained THROUGH it -> its fixed-slice score (0.887) was
  memorization. Lesson: a pinned eval slice must sit beyond the LARGEST train size you will EVER use (or use
  a disjoint split/dataset). Fix: head-to-head rerun @25000 for the two contenders.
