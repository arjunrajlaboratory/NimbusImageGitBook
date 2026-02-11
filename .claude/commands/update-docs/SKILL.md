---
name: update-docs
description: "Update NimbusImage GitBook documentation based on any input source (GitHub PR URL, text description, code, markdown docs). Analyzes the input to understand what needs documenting, finds the right location in the existing docs, writes content matching repo conventions, and creates a branch + PR. Use when the user wants to add or update documentation for a new feature, tool, workflow, or concept in the NimbusImage docs."
---

# Update NimbusImage Documentation

Add or update documentation in this GitBook repo based on input from any source.

## Accepted Input Types

- **GitHub PR URL**: Fetch with `gh pr view <URL> --json title,body` and read changed files
- **GitHub file URL**: Fetch with `gh api` to get raw content
- **Plain text**: User describes the feature or change
- **Code snippets**: Infer what needs documenting from the code
- **Markdown docs**: Adapt existing docs to GitBook style

## Workflow

### Step 1: Analyze the Input

Extract from the source material:
- What feature/tool/concept is being documented
- Key parameters, options, or configuration
- How users interact with it (workflow steps)
- Technical details relevant to users

For PR URLs, read the PR description and diff to understand the change. For code, identify user-facing behavior.

### Step 2: Find the Right Location

Read `SUMMARY.md` to understand the current doc structure, then determine placement:

| Content Type | Location | Action |
|---|---|---|
| New image processing tool (transforms images: crop, blur, deconvolution, etc.) | `documentation/image-processing.md` | Add new `##` section |
| New automated segmentation/detection tool (creates objects: Cellpose, Piscis, CondensateNet, etc.) | `documentation/analyzing-image-data-with-objects-connections-and-properties/tools-for-making-objects.md` | Add new `###` under "Automated object finding and connection" |
| New object/annotation feature | `documentation/analyzing-image-data-with-objects-connections-and-properties/` | Add to relevant subpage |
| New file format support | `documentation/images-datasets-and-collections/file-formats.md` | Add to existing page |
| New viewer feature | `documentation/viewing-your-data.md` | Add new section |
| New snapshot feature | `documentation/snapshots.md` | Add new section |
| Time-lapse feature | `documentation/time-lapse-mode.md` | Add new section |
| Entirely new topic area | `documentation/<new-dir>/README.md` | Create new subdir + update SUMMARY.md |
| Data management feature | `documentation/images-datasets-and-collections/managing-files.md` | Add to existing page |

Read the target page to understand existing content and style before writing.

### Step 3: Write Documentation

Match the conventions of this repo:

**Page structure for tools** (see image-processing.md pattern):
```
## Tool Name

Brief description of what the tool does and when to use it.

### How to use

1. **Step one** with bold lead-in
2. **Step two** continuing the workflow
3. ...

### Parameters

- **Parameter Name**: Description (range: X–Y, default: Z)
- ...

### Technical details

Explain how it works at a level useful to users, not implementation internals.
```

**Formatting conventions:**
- `#` page title, `##` sections, `###` subsections
- Images: `<figure><img src="../.gitbook/assets/filename.png" alt=""><figcaption></figcaption></figure>`
- Sized images: add `width="311"` to img tag
- Left-aligned images: wrap in `<div align="left">...</div>`
- Hints: `{% hint style="info" %}...{% endhint %}`
- Video embeds: `{% embed url="https://www.loom.com/share/..." %}`
- Bold lead-ins for list items: `- **Name**: description`
- Numbered lists for sequential steps, bullets for options/parameters
- User-focused tone — describe what users can do, not implementation details

**SUMMARY.md rules:**
- Update SUMMARY.md only when adding a new page (not when adding sections to existing pages)
- New pages in subdirectories: add as indented `* [Title](path)` under parent
- New top-level pages: add under the `## Documentation` group

### Step 3b: Update Citations (if applicable)

If the documented tool or algorithm has an associated **academic paper or software citation**, add it to `citations.md`. This applies to any tool that wraps or integrates third-party algorithms (e.g., Cellpose, Piscis, Deconwolf).

1. Read `citations.md` to understand the existing structure
2. Add a new `###` subsection under the `## Citations` heading (for algorithms/tools) or `## Packages` heading (for infrastructure/library dependencies)
3. Follow the existing pattern:
   ```
   ### Tool Name

   Brief description of what the tool does and its relevance to NimbusImage.

   Here is the GitHub repository:
   [https://github.com/...](https://github.com/...)

   Here is the paper:

   Author(s). (Year). [Title.](https://doi.org/...) _Journal_, Volume, Pages.
   ```
4. Include DOI links when available
5. If there are multiple papers (like Cellpose), list them all with a brief note about what each covers

**When to skip:** If the tool is entirely custom-built by the NimbusImage team with no external algorithm dependency, or if the citation already exists.

### Step 4: Create Branch and PR

1. Create a descriptive branch: `git checkout -b add-<feature>-docs`
2. Stage only the changed/new files
3. Commit with a clear message describing what was documented
4. Push and create a PR with:
   - Summary of what was added
   - Source of the information (PR link, etc.)
   - Test plan noting to verify GitBook rendering

## Documentation Areas Reference

The major areas of documentation and what belongs in each:

**Images, Datasets, and Collections** (`documentation/images-datasets-and-collections/`)
- Data organization: datasets (individual images), collections (groups), projects (publication-level)
- File formats and import (ND2, TIFF, PNG, etc.)
- Uploading, downloading, managing files

**Viewing Your Data** (`documentation/viewing-your-data.md`)
- Image viewer: layers, channels, contrast, navigation
- Z-stack and multi-position browsing
- Scale bar, overlays, display settings

**Analyzing Image Data** (`documentation/analyzing-image-data-with-objects-connections-and-properties/`)
- Objects: blobs, points, lines, polygons, freehand shapes
- Connections: relationships linking objects to each other
- Properties: measured values (intensity, area, etc.)
- Tags: labels for organizing/filtering objects
- Import/export of annotations and measurements

**Image Processing** (`documentation/image-processing.md`)
- Processing tools that transform images: Crop, Registration, Histogram Matching, Gaussian Blur, Deconvolution
- Each tool follows the How to use / Parameters / Technical details pattern
- Only for tools whose output is a processed image (shown in the "Original image" vs processed dropdown)

**Tools for Making Objects** (`documentation/analyzing-image-data-with-objects-connections-and-properties/tools-for-making-objects.md`)
- Automated segmentation/detection tools that create annotations: Cellpose, Cellpose-SAM, Piscis, CondensateNet
- Also covers manual tools (blob, point, line, rectangle) and Segment Anything
- Key distinction: if a worker from ImageAnalysisProject creates objects/annotations, it goes here; if it produces a processed image, it goes in image-processing.md

**Snapshots** (`documentation/snapshots.md`)
- Bookmarked views with specific visualization settings
- Exporting as images and movies

**Time Lapse Mode** (`documentation/time-lapse-mode.md`)
- Time-series specific features and workflows

**Top-level pages:**
- `quick-start.md` — Getting started walkthrough
- `new-features.md` — Changelog grouped by month (use `/update-changelog` skill instead)
- `vignettes.md` — Video tutorials (Loom embeds)
- `installation.md` — Self-hosted deployment
- `citations.md` — Algorithm citations
