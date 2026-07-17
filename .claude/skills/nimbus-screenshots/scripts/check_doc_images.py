#!/usr/bin/env python3
"""Check GitBook doc image references.

Run from the repo root:

    python3 .claude/skills/nimbus-screenshots/scripts/check_doc_images.py

Reports:
  * BROKEN — a doc references an asset that does not exist (fails the check)
  * ORPHAN — an asset in .gitbook/assets/ that no published doc references
            (informational only; e.g. old image (N).png files left after a refresh)

Exits non-zero if any broken references are found, so it can gate a PR.
Excludes .claude/ and CLAUDE.md (not part of the published GitBook site).
"""
import os
import re
import sys
import glob

ASSET_DIR = ".gitbook/assets"
ASSET_RE = re.compile(r"\.gitbook/assets/(.+?\.(?:png|jpe?g|gif|mp4|webm|svg))", re.IGNORECASE)


def iter_docs():
    for md in glob.glob("**/*.md", recursive=True):
        if md.startswith(".claude") or md == "CLAUDE.md" or "/.git" in md:
            continue
        yield md


def main() -> int:
    referenced = set()
    broken = []
    total_refs = 0
    for md in iter_docs():
        with open(md, encoding="utf-8") as fh:
            text = fh.read()
        for m in ASSET_RE.finditer(text):
            fn = m.group(1)
            referenced.add(fn)
            total_refs += 1
            if not os.path.exists(os.path.join(ASSET_DIR, fn)):
                broken.append((md, fn))

    on_disk = set()
    if os.path.isdir(ASSET_DIR):
        on_disk = {f for f in os.listdir(ASSET_DIR)
                   if os.path.isfile(os.path.join(ASSET_DIR, f))}
    orphans = sorted(on_disk - referenced)

    print(f"Checked {total_refs} references across "
          f"{sum(1 for _ in iter_docs())} docs.")
    if broken:
        print(f"\n{len(broken)} BROKEN reference(s):")
        for md, fn in sorted(broken):
            print(f"  {md}  ->  {fn}")
    else:
        print("No broken references. ✓")

    if orphans:
        print(f"\n{len(orphans)} orphaned asset(s) (not referenced by any doc):")
        for fn in orphans:
            print(f"  {fn}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
