# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **GitBook documentation repository** for [NimbusImage](https://app.nimbusimage.com), an open-source cloud-based image analysis platform for life science researchers (fluorescence microscopy, cell biology). The repo contains only Markdown content and image/video assets — there is no application code, build system, or test suite here.

## Repository Structure

- **`SUMMARY.md`** — GitBook table of contents. **Must be updated** whenever pages are added, removed, or reorganized.
- **`README.md`** — Landing page / homepage content.
- **Root-level `.md` files** — Top-level pages: `quick-start.md`, `vignettes.md`, `installation.md`, `citations.md`.
- **`documentation/`** — Main documentation content, organized into subdirectories by topic area. Each subdirectory has a `README.md` as its index page.
- **`.gitbook/assets/`** — All images (PNG, JPG) and videos (MP4) referenced by documentation pages. ~88 files.
- **`.claude/commands/nimbus-playwright.md`** — Custom Claude command (`/nimbus-playwright`) for automating documentation screenshots using Playwright MCP.
- **`.bookignore`** — Lists files excluded from the GitBook build (uses `.gitignore` syntax). Files listed here exist in the repo but are invisible to readers and inaccessible via URL. This file itself, `CLAUDE.md`, is excluded via `.bookignore`.

## Content Conventions

- GitBook image references use the `<figure>` tag format:
  ```markdown
  <figure><img src="../.gitbook/assets/filename.png" alt=""><figcaption></figcaption></figure>
  ```
- Video tutorials are embedded via Loom URLs using GitBook's embed syntax.
- Pages can have YAML frontmatter (`description`, `cover`, `coverY`).
- GitBook auto-generates commits prefixed with `GITBOOK-XX:`.

## Working with This Repo

**Adding a new page:**
1. Create the `.md` file in the appropriate location.
2. Add an entry to `SUMMARY.md` — this is what controls GitBook's sidebar navigation.
3. Place any images in `.gitbook/assets/`.

**Adding non-published files:**
If you add Markdown or other files that should live in the repo but **not** appear in the published GitBook site (e.g., internal notes, tooling configs), add them to `.bookignore`. Without this, orphaned Markdown files may still be reachable via direct URL even if they aren't in `SUMMARY.md`.

**Taking documentation screenshots:**
Use the `/nimbus-playwright` command, which provides a full workflow for capturing annotated screenshots of the NimbusImage app using Playwright MCP tools. Screenshots go to `.playwright-mcp/` and should be copied to `.gitbook/assets/` for use in docs.

## Key Domain Concepts

The documentation covers NimbusImage's core concepts, which are important to understand when editing content:

- **Datasets** — Individual image files uploaded to the platform.
- **Collections** — Groups of related datasets.
- **Projects** — Higher-level groupings of datasets and collections with publication metadata.
- **Objects** — Analysis primitives (blobs, points, lines, polygons, freehand shapes) drawn on images.
- **Connections** — Relationships linking objects to each other (e.g., spots to cells).
- **Properties** — Measured values computed for objects (intensity, area, etc.).
- **Tags** — Labels for organizing and filtering objects.
- **Snapshots** — Bookmarked views of data with specific visualization settings, exportable as images/movies.

## NimbusImage Application Repo

The main application source code lives at https://github.com/arjunrajlaboratory/NimbusImage/. When asked, you can inspect PRs and recent changes there (via `gh`) to identify new or changed features that need documentation updates in this repo.

## Git Workflow

PR-based workflow using GitHub CLI (`gh`). The `.claude/settings.local.json` has permissions pre-configured for git operations and GitHub PR management.
