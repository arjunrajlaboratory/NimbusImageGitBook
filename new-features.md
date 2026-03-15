# New features

Stay up to date with the latest additions to [NimbusImage](https://app.nimbusimage.com).

## March 2026

### Few-shot segmentation with SAM

Use a few example annotations to automatically find and segment similar objects across your image. Two model options are available: SAM1 (ViT-H) for higher quality results and SAM2 (Base+) for faster processing.

**TSV export support** — Export your annotation data as tab-separated values (TSV) in addition to CSV. A format toggle in the export dialog lets you switch between CSV and TSV. TSV is recommended when property names contain commas, and the dialog will warn you when this is the case.

**Increased batch dataset limit** — Automated annotation workers can now be applied to up to 50 datasets in a collection at once, up from 10.

**Side panels push content** — The object list, snapshots, and settings panels now push the image viewport to the side instead of overlaying it, so you can see your image and panel contents at the same time. Panels also stay open when interacting with the image.

#### Bug fixes

* Fixed CSV export where selecting individual properties to export would check or uncheck all properties at once.
* Fixed comma handling in property names: property auto-naming now uses spaces instead of commas between tags, and property names containing commas are properly quoted in CSV exports.
* Fixed layer and annotation renaming showing "\[object Event]" instead of the typed name.
* Fixed worker tool settings being lost when closing and reopening the tool panel.
* Fixed the collection name label overlapping the input text on the dataset info page.
* Fixed tooltips on dataset info collection buttons rendering as a narrow vertical stripe.
* Fixed upload progress bar stuck at "0 B / 0 B".
* Fixed login form not appearing on the home page.

## February 2026

### Circle and ellipse annotation tools

Draw circular and elliptical regions on your images. The circle tool inscribes a circle within your drag area, while the ellipse tool fills the full bounding box. Both are measured like other polygon-based objects.

### Combine annotations tool

Merge two polygon annotations into one by clicking them in sequence. Works with overlapping or nearby polygons, with a configurable tolerance for how close shapes need to be. Connections from the merged annotation are automatically preserved.

### Batch annotation computation

Apply automated annotation computations across all datasets in a collection at once. A progress bar tracks each dataset, and you can cancel the batch at any time.

### Project sharing

Share entire projects with other users and control their access level. When you share a project, permissions automatically propagate to all datasets, collections, and views within it. Making a project public also makes all its contents publicly accessible.

**Sharing status indicators** — See at a glance who has access to your datasets and configurations, with color-coded badges showing read, write, and admin access levels.

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

### Deconwolf deconvolution

Deconvolve 3D fluorescence microscopy Z-stacks using the Richardson-Lucy algorithm. Supports GPU acceleration for faster processing, with automatic CPU fallback. Optical parameters can be auto-extracted from ND2 metadata, and large images are automatically tiled to fit in memory.

**Piscis PyTorch update** — The Piscis spot detection workers have been updated to the official v1.0.0 release with a PyTorch backend. The default detection threshold is now 0.5 (previously 1.0) for improved sensitivity.

**Dimension slider step arrows** — Use up/down arrow buttons next to XY, Z, and Time sliders to step through values one at a time.

#### Bug fixes

* Fixed login requiring a double click.

## December 2025

### CondensateNet automated condensate segmentation

Automatically detect and segment biomolecular condensates in fluorescence microscopy images using the CondensateNet deep learning model.

**Improved upload dialog** — The upload dialog now includes a name picker and location picker, with duplicate name checking.

**Text or number labels** — Toggle between showing descriptive text labels (e.g., "Well A1") or numeric labels in the viewer settings.

**Smarter folder defaults** — When adding a dataset to an existing collection, the file browser now defaults to the dataset's current folder instead of your private folder.

## November 2025

### Refreshed home page

The home page now has a single unified upload button, a tabbed interface for recent and sample datasets, updated guided tours, and improved dark mode support.

#### Bug fixes

* Fixed the unroll checkbox disappearing when selected.
