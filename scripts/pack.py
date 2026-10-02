"""Package regdoor/ into dist/regdoor-plugin-<version>.zip for upload to claude.ai / Claude Desktop.

PowerShell's Compress-Archive writes entry names with backslashes, which Anthropic's
uploader rejects ("Zip file contains path with invalid characters"). This script always
writes forward-slash entry names, UTF-8 flagged, with the manifest at the zip root.
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "regdoor"
EXCLUDE_DIRS = {"__pycache__", ".git", "node_modules"}


def main() -> int:
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / f"regdoor-plugin-{version}.zip"
    if out.exists():
        out.unlink()
    files = sorted(
        p for p in PLUGIN.rglob("*")
        if p.is_file() and not (EXCLUDE_DIRS & set(p.relative_to(PLUGIN).parts))
    )
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            arcname = path.relative_to(PLUGIN).as_posix()
            zf.write(path, arcname)
    with zipfile.ZipFile(out) as zf:
        names = [i.orig_filename for i in zf.infolist()]
    bad = [n for n in names if "\\" in n or n.startswith("/")]
    if bad:
        print("invalid entry names:", bad, file=sys.stderr)
        return 1
    if ".claude-plugin/plugin.json" not in names:
        print("manifest missing from zip root", file=sys.stderr)
        return 1
    print(f"created {out} ({out.stat().st_size} bytes, {len(names)} entries)")
    for n in names:
        print("  ", n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
