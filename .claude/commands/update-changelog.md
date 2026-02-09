# Update Changelog

Populate the **New features** page (`new-features.md`) with user-facing changes from recently merged PRs in the NimbusImage application repo.

## Arguments

This skill accepts an optional argument to skip the deployment delay filter:

- `/update-changelog` — normal mode (excludes PRs merged < 7 days ago)
- `/update-changelog --include-recent` — include all merged PRs regardless of deployment delay

## Workflow

Follow these steps in order:

### 1. Read the changelog page

Read `new-features.md` in the repo root. If it does not exist, create it from this template and add it to `SUMMARY.md` after "Quick start":

```markdown
---
description: Stay up to date with the latest additions to NimbusImage
---

# New features

Stay up to date with the latest additions to [NimbusImage](https://app.nimbusimage.com).
```

### 2. Extract already-documented entries

Scan the contents of `new-features.md` for existing entries. Look at the `###` headings (major features), `**bold**` titles (minor improvements), and bug fix bullets to build a list of what's already documented. Use these to avoid duplicates — match on feature name/topic, not PR numbers (since entries don't cite PRs).

### 3. Determine the date cutoff

- If there are already-documented entries, look at the most recent `## Month Year` heading and use the first day of that month as the cutoff — re-check PRs from that month onward in case new ones have been added.
- If the changelog is empty (first run), use **90 days ago** as the cutoff.

### 4. Fetch merged PRs

```bash
gh pr list --repo arjunrajlaboratory/NimbusImage --state merged --limit 100 --json number,title,body,mergedAt,labels --jq '[.[] | select(.mergedAt > "CUTOFF_DATE")]'
```

Replace `CUTOFF_DATE` with the ISO date from step 3.

### 5. Filter out PRs not yet deployed

**Skip this step if the user passed `--include-recent`.**

NimbusImage features take approximately **7 days** after PR merge to reach production. Remove any PR merged **less than 7 days ago** from the list. For each remaining PR, compute its "available date" as `mergedAt + 7 days` — this is the date shown to readers.

If `--include-recent` was passed, keep all PRs and still compute the available date as `mergedAt + 7 days` for display grouping purposes, but note in the output that recently merged PRs may not yet be live.

### 6. Classify PRs

For each remaining PR, classify it along two dimensions:

1. **Audience**: user-facing vs. internal
2. **Type & significance**: major feature, minor improvement, bug fix, or internal

#### Audience: User-facing vs. Internal

First, determine whether the PR affects what users see or do:

**User-facing (INCLUDE):**
- New features, tools, UI elements, or workflows
- Redesigns or significant UX improvements
- New export/import capabilities
- Bug fixes that users would have noticed
- Performance improvements users would feel

**Internal (SKIP):**
- Titles containing: "Refactor", "Fix lint", "Update dependencies", "CI", "CD", "Bump", "Chore", "Internal", "Cleanup"
- Code refactoring, dependency updates, CI/CD changes, linting fixes, test infrastructure, developer tooling, internal config changes
- Admin-only features (e.g., Girder links for admins)
- PRs with labels like `internal`, `dependencies`, `ci`

#### Type & significance: Major, minor, or bug fix

For each user-facing PR, classify its significance:

**Major feature** — Substantial new capability or workflow:
| PR Title | Why major |
|----------|-----------|
| "Add Projects feature" | Entirely new organizational concept |
| "Upload multiple datasets" | New batch workflow |
| "Public access" | New sharing model |
| "Redesign tool selection UI" | Complete UI overhaul of core interaction |

**Minor improvement** — Incremental enhancement to existing functionality:
| PR Title | Why minor |
|----------|-----------|
| "Add up/down step arrows to dimension sliders" | Small UX addition to existing control |
| "Add option to display text or number labels" | New toggle on existing feature |
| "Adjust default annotation settings" | Better defaults, no new capability |
| "Allow for current folder in ImportConfiguration" | Small workflow improvement |

**Bug fix** — Corrects broken or unexpected behavior:
| PR Title | Why bug fix |
|----------|-------------|
| "Fix the unroll checkbox disappearing" | UI element was broken |
| "Fix the need to double click on the login button" | Interaction was broken |

#### Ambiguous (ASK USER)

If a PR doesn't clearly fit, present it to the user with title, body summary, and your best guess for audience + significance. Ask whether to include or skip.

### 7. Remove already-documented entries

From the classified user-facing PRs, remove any that are already covered in the changelog (matched by topic/feature name in step 2).

### 8. Draft changelog entries

For each remaining user-facing PR, write a changelog entry. Do **not** include PR numbers or links to GitHub — entries should read as a clean user-facing changelog.

The format differs by type:

#### Major features

```
### Feature title

Description of what users can now do — 2-3 sentences focusing on user benefit.
```

Major features get an `###` heading and a longer description.

**Good example:**
> ### Projects
>
> Group your datasets and collections into projects for publications. Add metadata like authors, license, DOI, and keywords to prepare your data for sharing and citation.

#### Minor improvements

```
**Title** — One sentence description of the improvement.
```

**Good example:**
> **Dimension slider step arrows** — Use up/down arrow buttons next to XY, Z, and Time sliders to step through values one at a time.

#### Bug fixes

Bug fixes are grouped together under a "Bug fixes" subheading within each month, using a compact bullet format:

```
#### Bug fixes

- Fixed issue where the unroll checkbox would disappear when selected.
- Fixed login requiring a double click.
```

#### Writing guidelines (all types):

- **Title**: Concise noun phrase from the user's perspective (e.g., "Polygon object tool", not "Add polygon object tool implementation")
- **Description**: Focus on user benefit, not implementation details. What can the user do now that they couldn't before?
- Do NOT use overly technical language or reference code internals
- Do NOT include PR numbers, GitHub links, or other source references
- Bug fix descriptions should say what was broken, not how it was fixed

**Bad example (too technical):**
> **Add polygon tool** — Implemented a new polygon vertex-based SVG rendering path with hit-testing in the canvas overlay component.

### 9. Group entries by month

Group the drafted entries by **month** based on their "available date" (merge date + 7 days, from step 5). Within each month, order by significance: major features first, then minor improvements, then bug fixes.

Format:

```markdown
## Month Year

### Major feature title

Description.

**Minor improvement title** — Description.

**Another minor improvement** — Description.

#### Bug fixes

- Fixed thing that was broken.
```

Order: newest month first at the top, oldest at the bottom.

When adding to an existing changelog, merge new entries into existing month sections where appropriate rather than creating duplicate month headings.

### 10. Present and write

**Present** all drafted entries to the user for review before writing anything. Show them grouped by month with the major/minor/bugfix structure. Ask:

> Here are the new changelog entries I'd like to add. Should I proceed, or would you like changes?

Once approved, write the entries into `new-features.md`, placing new months after the intro paragraph and before any existing month sections (so newest content is always at the top).

## Edge cases

- **First run (empty changelog)**: Use 90-day lookback. The intro paragraph already exists in the template; add month sections after it.
- **No new PRs found**: Report "No new user-facing changes found since [date]." and exit without modifying the file.
- **Month boundary**: A PR merged on Jan 30 with +7 days available Feb 6 goes under "February 2025", not January.
- **Multiple PRs for same feature**: If several PRs clearly implement parts of the same feature, combine them into a single entry.
