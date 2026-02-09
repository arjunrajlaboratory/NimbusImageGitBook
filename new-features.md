# New features

Stay up to date with the latest additions to [NimbusImage](https://app.nimbusimage.com).

## February 2026

### Circle and ellipse annotation tools

Draw circular and elliptical regions on your images. The circle tool inscribes a circle within your drag area, while the ellipse tool fills the full bounding box. Both are measured like other polygon-based objects.

### Combine annotations tool

Merge two polygon annotations into one by clicking them in sequence. Works with overlapping or nearby polygons, with a configurable tolerance for how close shapes need to be. Connections from the merged annotation are automatically preserved.

### Batch annotation computation

Apply automated annotation computations across all datasets in a collection at once. A progress bar tracks each dataset, and you can cancel the batch at any time.

**SAM model options** — Choose between SAM1 (ViT-B), SAM2 Base+, and SAM2 Large for AI-assisted segmentation, giving you more control over speed vs. quality.

**MP4 movie export** — Export snapshot movies as MP4 in addition to WebM, with broader browser compatibility including Safari.

**Bulk collection export** — Export annotations for every dataset in a collection as individual JSON files with a single click.

**Upload dialog help** — An info button in the upload dialog explains what datasets, batch mode, and collections are.

**Dataset statistics** — The dataset info page now shows counts for annotations, connections, properties, and property values.

**Upload configuration redesign** — The multi-file dataset configuration view now uses a visual badge and slot layout, making it easier to see and assign variables to dimensions like XY, Z, Time, and Channel.

**Filename variable highlighting** — When uploading multi-file datasets, an interactive preview highlights which parts of your filenames correspond to which dimensions, with color-coded segments and a legend.

**Improved annotation defaults** — Annotations now maintain a consistent size regardless of zoom level and use a smaller, less obtrusive marker size by default.

**Large dataset exports** — CSV and JSON exports now handle large datasets (tens of thousands of annotations) without browser memory issues.

**CondensateNet large image support** — The CondensateNet segmentation worker can now process large images by automatically tiling them, stitching objects across tile boundaries.

#### Bug fixes

* Fixed CondensateNet segmentation failing on images with non-standard dimensions.

## January 2026

### Projects

Group your datasets and collections into projects for publications. Add metadata like authors, license, DOI, and keywords to prepare your data for sharing and citation.

### Batch dataset upload

Upload multiple files at once, creating one dataset per file within a collection. Supports both quick and advanced import modes, with shared dimension configuration across all datasets.

### Public dataset sharing

Make any dataset publicly accessible via a link — no account required to view.

### Redesigned sharing dialog

Manage who has access to your datasets in real time. See current users, change permission levels, add or remove access, and toggle public visibility from one unified dialog.

### Redesigned tool selection

The tool creation dialog now groups tools by category with color-coded sections, descriptions for each tool, and a featured tools section at the top.

**Dimension slider step arrows** — Use up/down arrow buttons next to XY, Z, and Time sliders to step through values one at a time.

#### Bug fixes

* Fixed login requiring a double click.

## December 2025

**Improved upload dialog** — The upload dialog now includes a name picker and location picker, with duplicate name checking.

**Text or number labels** — Toggle between showing descriptive text labels (e.g., "Well A1") or numeric labels in the viewer settings.

**Smarter folder defaults** — When adding a dataset to an existing collection, the file browser now defaults to the dataset's current folder instead of your private folder.

## November 2025

### Refreshed home page

The home page now has a single unified upload button, a tabbed interface for recent and sample datasets, updated guided tours, and improved dark mode support.

#### Bug fixes

* Fixed the unroll checkbox disappearing when selected.
