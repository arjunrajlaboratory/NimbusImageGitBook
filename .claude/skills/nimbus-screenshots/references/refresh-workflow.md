# Refreshing stale documentation screenshots

The end-to-end workflow for a "the screenshots are out of date, redo them" pass
(as opposed to `update-docs`, which adds *new* content from a source). Pair this
with the capture mechanics in the parent `SKILL.md`.

## 1. Audit what exists

Find every image reference and how many each doc has:

```bash
grep -roE "\.gitbook/assets/[^\")>]+" --include='*.md' . | sort | uniq -c
```

GitBook references come in a few shapes — handle all of them:
- `<figure><img src="../.gitbook/assets/FILE.png" alt="" width="156"><figcaption>…</figcaption></figure>`
- `<div align="left"><figure>…</figure></div>` (constrained width / left-aligned)
- `![](<.gitbook/assets/FILE.png>)` (older inline syntax)
- `cover:` / frontmatter references

Old GitBook auto-generated names look like `image (31).png`, `image (1) (1).png`.
Descriptive names (`3d-volume-visualization.png`, `viewer-minimap.png`) are the
current convention and are almost always the *up-to-date* ones — leave those.

Read each doc to learn **what each figure is supposed to show** before recreating it.

## 2. Map each shot to a dataset and capture

Group shots by the app view/state they need so you visit each dataset once
(e.g. viewer overview + minimap + layer grouping all come from one dataset).
Ask the user for representative datasets (a general one, one with many
annotations, one with computed properties, a time-lapse). **Only local
`localhost:5173` datasets load** in the automation browser — `app.nimbusimage.com`
IDs 404. Capture with the chrome-devtools workflow in the parent SKILL.md.

## 3. Replace, preserving layout

- Save new files with **descriptive names** into `.gitbook/assets/`.
- **Do not overwrite or delete the old `image (N).png` files** — just point the
  markdown at the new file. The old ones become harmless orphans (see step 5).
- In the markdown, change only the `src=`; **keep the existing `width` and
  `<figcaption>`** unless the caption is now wrong. Match the surrounding figure
  syntax (`<figure>` vs `<div align="left">` vs `![]()`).

## 4. Fix prose where the UI *changed*, not just where it looks different

The biggest trap: an out-of-date screenshot often means the *workflow* changed,
so the surrounding text is wrong too. Examples found in the July 2026 pass:
- Layer grouping: drag-to-"drop-zone" → a **"Make layer group…"** menu
- "Click `+` next to Toolset" → **"Add new tool"** button in the Tools panel
- The measure-properties flow (tag → algorithm → options) → a single **Measure
  objects** panel (measure by tag/shape → Create Property → "Show in annotation
  list" → column)
- CSV/JSON export moved from the Object Browser **ACTIONS** menu → the top-bar
  **Import / export data** menu

When the steps changed, rewrite the numbered steps / prose to match, not only the image.

## 5. Verify before the PR

```bash
python3 .claude/skills/nimbus-screenshots/scripts/check_doc_images.py
```

Must report **0 broken references**. It also lists orphaned assets — the old
`image (N).png` files you just replaced will show up there, which is expected and
harmless (this repo has always carried orphans). Don't bulk-delete them as part of
a screenshot refresh unless the user asks; deleting data is their call.

## 6. Canvas interactions the automation can't do

geojs (the viewer engine) accepts synthetic **wheel** events (so programmatic
zoom works) but **ignores synthetic mouse drag/draw** events. So anything that
needs a real drag/draw/drop on the canvas — drawing blobs, shift-drag selection,
dropping a file on the upload zone — must be done **collaboratively**: set up the
view, ask the user to perform the gesture in the automation window, wait for
"done", then capture. This worked well for the upload drop, the shift-drag
selection popup, and drawing blobs.

Things that genuinely need extra setup (worker runs, multi-layer time offsets) or
can't be reproduced locally (NimbusImage.com-only team folders) are fair to defer
— note them explicitly in the PR rather than leaving them silently stale.
