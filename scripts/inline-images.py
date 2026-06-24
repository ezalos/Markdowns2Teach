# ABOUTME: Post-processes Marp HTML files to fix SVG background-image rendering.
# ABOUTME: Injects a preloader script that loads images before SVG paint, fixing race conditions.

import re
import sys
from pathlib import Path

PRELOADER_SCRIPT = """<script>
// Preload all background images used in Marp SVG slides, then force repaint.
// Marp renders slides as SVG foreignObject; if background-image loads after
// initial SVG paint, the image never appears without a manual resize/reload.
(function() {
  function extractUrls() {
    var urls = [];
    var figures = document.querySelectorAll('figure[style*="background-image"]');
    figures.forEach(function(fig) {
      var m = fig.style.backgroundImage.match(/url\\("?([^"\\)]+)"?\\)/);
      if (m && m[1] && !m[1].startsWith('data:')) urls.push(m[1]);
    });
    var imgs = document.querySelectorAll('img[src]');
    imgs.forEach(function(img) {
      if (img.src && !img.src.startsWith('data:')) urls.push(img.src);
    });
    return urls;
  }
  function preloadAndRepaint() {
    var urls = extractUrls();
    if (urls.length === 0) return;
    var loaded = 0;
    var total = urls.length;
    function onDone() {
      loaded++;
      if (loaded >= total) {
        // Force SVG repaint by toggling a parent style
        var svgs = document.querySelectorAll('svg[data-marpit-svg]');
        svgs.forEach(function(svg) {
          svg.style.opacity = '0.999';
          requestAnimationFrame(function() {
            svg.style.opacity = '';
          });
        });
        // Also trigger resize event which Marp's polyfill listens to
        window.dispatchEvent(new Event('resize'));
      }
    }
    urls.forEach(function(url) {
      var img = new Image();
      img.onload = onDone;
      img.onerror = onDone;
      img.src = url;
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', preloadAndRepaint);
  } else {
    preloadAndRepaint();
  }
})();
</script>"""


def inject_preloader(html_path: Path) -> None:
    """Inject an image preloader script before the closing </body> tag."""
    content = html_path.read_text()

    # Check if preloader is already injected
    if "preloadAndRepaint" in content:
        return

    # Inject before closing </body> if present, otherwise before </html>
    if "</body>" in content:
        content = content.replace("</body>", PRELOADER_SCRIPT + "\n</body>", 1)
    elif "</html>" in content:
        content = content.replace("</html>", PRELOADER_SCRIPT + "\n</html>", 1)
    else:
        # Append at end
        content += "\n" + PRELOADER_SCRIPT

    html_path.write_text(content)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: inline-images.py <html_dir>", file=sys.stderr)
        sys.exit(1)

    html_dir = Path(sys.argv[1])
    for html_file in sorted(html_dir.rglob("*.html")):
        if html_file.name == "index.html":
            continue
        rel = html_file.relative_to(html_dir)
        print(f"  PRELOAD: {rel}")
        inject_preloader(html_file)


if __name__ == "__main__":
    main()
