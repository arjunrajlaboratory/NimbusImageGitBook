---
description: >-
  Explore spatial-transcriptomics data such as 10x Xenium: view individual
  molecules, use any gene as a measurement, compare expression between groups,
  and compute neighborhood and region statistics
---

# Spatial transcriptomics

NimbusImage can hold a whole spatial-transcriptomics run in one place: the tissue images, every segmented cell, the full gene-expression table for every cell, and the individual detected molecules. Everything you already use for cell analysis — filters, the Analysis panel, gates, color-by-property, CSV export — works on genes too, so you can, for example, gate on two genes in a scatter plot and then look at where those cells sit in the tissue.

The feature was built around **10x Xenium** output bundles (Xenium Onboard Analysis 1.3 through 4, including Prime 5K and the XOA 4 protein panels). It has been used on datasets with over 700,000 cells and more than 4,600 genes.

## The workflow at a glance

1. **Ingest** a Xenium bundle with the `nimbusimage` Python tooling. This creates the image datasets, draws a polygon for every cell, and registers the expression table and the molecules.
2. **Look at molecules** with the **Transcripts** palette — individual points when zoomed in, a density heat map when zoomed out.
3. **Use genes as measurements**: add genes as live columns, copy them into a stored measurement, or compute a gene-set score. Genes then work in filters, plots, gates and color-by.
4. **Ask questions** from the **Selection summary**: composition and mean expression of a population, differential expression between two groups, neighborhood enrichment between cell types, and per-region summaries.
5. **Edit cells and recompute**: if you redraw, add or delete cell outlines, rebuild the expression table from the molecules. Earlier tables are kept as versions you can switch between.

## Getting your data in

Loading a Xenium bundle is done with the **xenium-ingest** tooling in the `nimbusimage` Python package, not through the upload page. It is usually run by whoever administers your server, or by an AI coding assistant such as Claude Code (the package ships an `xenium-ingest` skill with the full runbook). If you don't have access to run it yourself, ask your server administrator to ingest the bundle.

### What files are needed

From the 10x download, the ingest uses:

* **The output bundle** (`*_xe_outs.zip`), from which it needs `morphology_focus/`, `cells.zarr.zip` (cell outlines), `cell_feature_matrix.zarr.zip` (the counts), `analysis.zarr.zip` (clusterings), `experiment.xenium` (pixel size and run details) and, for the molecule overlay, `transcripts.zarr.zip`
* **The H&E image** (`*_he_image.ome.tif`) and its **alignment matrix** (`*_he_imagealignment.csv`), if you want the H&E as well
* **Cell types** (`*_cell_types.csv`), if 10x provides them for your dataset
* **Pathology regions** (`*_annotation.geojson`), optionally

### Running the ingest

The tooling is installed with `pip install 'nimbusimage[xenium]'` (use `nimbusimage[xenium-umap]` to also compute a UMAP). Every step is available both as a Python function and as a subcommand of the `nimbusimage-xenium` command; `nimbusimage-xenium <step> --help` lists each step's options. In order, the steps are:

1. **`morphology`** — create the image dataset from `morphology_focus/`, with channels named after their stains (for example `c00-DAPI`)
2. **`polygons`** — draw one polygon per segmented cell, and save a *cell map* file that later steps reuse
3. **`umap`** — compute a UMAP embedding (10x does not ship one)
4. **`properties`** — write a marker-gene panel, clusterings and the UMAP coordinates as measurements
5. **`cell-types`** — tag each cell with its type
6. **`spatial-table`** — build and register the full expression table
7. **`transcripts`** — register the molecules as an overlay
8. **`regions`** — import pathology regions as polygons tagged `region`

{% hint style="info" %}
Try each upload step on a small slice first (`--limit 2000`) and check the result in the viewer before running the full dataset.
{% endhint %}

### What you end up with

* **Two datasets**: a **morphology dataset** with the fluorescence stains (protein bundles can have ~35 channels), and a separate **H&E dataset**. The H&E is imaged on its own pixel grid, so the ingest uses 10x's alignment matrix to place cells, regions and molecules correctly on it.
* **Cell polygons**, one object per segmented cell, each tagged `cell` plus its cell type (for example `Memory B Cell`)
* **Measurements** such as `Gene Expression` (the marker panel), `Clustering` (for example `graphclust`) and `UMAP` (`x`, `y`)
* **A spatial expression table** with *every* gene for every cell. On protein bundles, antibody targets are named `<name> (protein)` (for example `CD4 (protein)`) so they don't collide with the gene of the same name.
* **A transcripts overlay** of the individual molecules
* Optionally, **pathology regions** as polygons tagged `region`

A new collection shows at most 6 channels as layers; use **Add layer** in the Layers panel to show the rest.

### How cells relate to the expression table

Each row of the expression table belongs to exactly one cell polygon. The table keeps all genes in a single file on the server rather than as millions of stored measurement values, which is what makes a whole-transcriptome table practical. Cells you add later have no row until you [recompute the table](#editing-cells-and-recomputing-the-table); an analysis that finds objects without a row reports them (for example "N of the summarized objects have no row in the spatial table").

### Importing pathology regions yourself

Region layers drawn in QuPath or shipped by 10x can also be imported from the app:

1. Open the **Import / export data** menu (up/down-arrows icon in the top bar) → **Import GeoJSON…**
2. Choose the `.geojson` or `.json` file and check the **Preview** (counts by shape and by class)
3. Pick the **Layer (sets the channel)**
4. Keep **Extra tag for every annotation** as `region` (the default); each feature's class name also becomes a tag
5. Click **Import**

Coordinates are read as this image's pixels, with the origin at the top-left (QuPath's convention). A warning appears if coordinates fall outside the image, which usually means the file is in microns or belongs to the other image — files drawn on the H&E image must be imported on the **H&E dataset**. **Export GeoJSON** in the same menu does the reverse, for use in QuPath and similar tools.

{% hint style="warning" %}
**Keep the `region` tag on regions, never on cells.** Neighborhood, region summaries and recompute treat polygons tagged `region` as regions rather than cells. A region without the tag would be counted as one giant cell; a cell with it would be left out of those analyses.
{% endhint %}

## Viewing molecules: the Transcripts palette

On datasets with registered transcripts, a **Transcripts** button (hexagon-of-dots icon) appears in the palette toolbar.

1. Open **Transcripts** and turn on **Show transcripts**
2. Search for and pick genes in **Genes (up to 8)**. Each gets its own color, which you can change next to the gene name
3. Adjust **Quality ≥** (default 20, Xenium's own cut-off) and **Opacity**
4. Choose a **Rendering** mode:
   * **Auto** — individual molecules as points when zoomed in, a density **Heat map** when zoomed out
   * **Points** or **Heat map** to force one
5. **Points on screen at most** caps how many molecules are drawn at once

**Clicking a molecule** shows its gene, position and quality. If it lies inside a cell outline, **Go to cell** jumps to and selects that cell.

A few things to know:

* **The status line** under the controls says what is being shown — a number of molecules, or "Density heat map"
* **Zoomed out, the quality threshold is approximate**: points are merged into clusters, and the heat map counts molecules of every quality. Zoom in for an exact threshold
* **On the H&E dataset only points are available** — there is no heat map there

To see every cell at once rather than a subset, see the zoomed-out overview in [Working with large annotation datasets](large-annotation-datasets.md).

## Genes as measurements

Every gene in the expression table can be used like any other measurement.

1. Open the **Object Browser** and go to the **Measurements** tab
2. Click **Add genes** (DNA icon). The button only appears when the dataset has an expression table
3. Search for and pick genes, then choose one of three modes:
   * **Add as live columns** (the default) — genes are read straight from the table, instantly. They work in filters, plots, color-by, the object list and CSV export, but you can't sort the object list by them
   * **Copy into a measurement** — writes each gene's count for every cell as a stored value under a **Measurement name** (default `Gene Expression`). Stored values are sortable and exportable. On large datasets this runs as a server job
   * **Gene-set score** — writes one value per cell, the **mean** (default) or **sum** of the picked genes, under a **Score name** you choose. Scores are stored in a `Gene set scores` measurement
4. Click the button at the bottom (for example **Add 3 genes as columns**, **Copy 3 genes** or **Score 3 genes**)

Live gene columns are listed under a single **Spatial table** group in the Measurements tab, without a **Run** button, since there is nothing to compute. From there they behave like the rest of your properties:

* **Showing values** — show and hide them as columns in the object list, as described in [Finding and showing measurements](interacting-with-objects.md#finding-and-showing-measurements)
* **Filtering** — use them in property filters, like any numeric property
* **Coloring** — pick a gene in [Color by Property](interacting-with-objects.md#coloring-objects-by-a-property-value). For cluster ids, choose **Categorical**, since **Auto** may give integer clusters a continuous ramp
* **Plotting and gating** — use genes as axes in the [Analysis panel](analysis-plots-and-gating.md) and draw gates on them
* **Exporting** — CSV export includes live columns, named `spatial / <gene>`

Cell types arrive as tags, and categorical measurements such as clusters can be filtered as described in [Filtering by text-valued properties](interacting-with-objects.md#filtering-by-text-valued-properties).

## Analyses

All the spatial analyses start from the **Selection summary**: open the **Import / export data** menu (up/down-arrows icon in the top bar) → **Selection summary**.

### Selection summary

**What it answers:** what is in this population, and how much do its cells express a given gene?

1. Choose **Objects to summarize**: **All objects**, **Filtered objects** (your current filters and gates), or **Selected objects**
2. Read the **Composition by tag** table — count and percentage for each tag, which for Xenium cells means each cell type
3. Optionally pick **Properties to summarize** to get n, mean, SD, min and max for each
4. In the **Expression** section, pick genes under **Genes from the spatial table** to see each gene's **Mean count** and **% expressing** over the same objects
5. **Download CSV** saves the summary, expression included

Mean counts include cells with zero counts.

### Differential expression

**What it answers:** which genes are most differently expressed between two groups of cells?

1. In the Selection summary, choose **Filtered objects** or **Selected objects** — this is **group A**. (The button is disabled for **All objects**, since there would be nothing to compare against.)
2. In the **Expression** section, click **Compare expression…**
3. Choose **group B**: **B: everything else** (the default) or **B: objects with any of these tags**
4. Choose the test: **Welch t-test** (the default) or **Wilcoxon (Mann-Whitney)**
5. Set **Genes to list** (default 50, up to 500) and click **Compare**

Every gene in the table is tested. The result is a ranked table with each gene's **log₂ FC**, **Mean A**, **Mean B**, **% A**, **% B**, the test statistic and **p**, along with the number of cells in each group and the number of genes tested. A positive log₂ fold change means higher in A. **Download CSV** saves the table.

### Neighborhood enrichment

**What it answers:** which cell types sit next to which, more or less often than expected by chance?

1. In the Selection summary, under **Spatial statistics**, click **Neighborhood…**
2. Set the **Radius (µm)** (default 30)
3. Check **Tags that are not types** (default `cell`): tags listed here are ignored when deciding each cell's type
4. Click **Compute**

Each cell's neighbors within the radius are counted by type, where a cell's type is its first tag not in the ignore list. The result is a matrix of log₂ observed / expected neighbor pairs between every pair of types — positive values mean two types are neighbors more often than expected if the type labels were shuffled. Hover over a cell of the matrix for its value; **CSV** downloads it. Each cell's neighbor fractions by type are also saved as a `Neighborhood` measurement, so you can filter, gate and color by them.

The radius needs the dataset's pixel size. When it is blank, NimbusImage fills it in from the expression table, including on the H&E dataset; the hint under the radius shows the conversion to image pixels.

### Region summaries

**What it answers:** how many cells of each type, and how much expression, fall inside each tissue region?

1. In the Selection summary, under **Spatial statistics**, click **Regions…**
2. Choose **Polygons with a tag** and pick the **Region tag** (for example `region`), or **Selected polygons** (up to 50)
3. Optionally pick **Genes (mean per region)**
4. Click **Summarize**

Each row shows a region, its number of cells and their composition by type, plus the mean count of each chosen gene. A cell belongs to a region when its center lies inside the region polygon. **CSV** downloads the table.

## Editing cells and recomputing the table

When you redraw, add or delete cell outlines, the expression table no longer matches your cells. You can rebuild it from the molecules: every molecule is assigned to the cell polygon it falls in (the smallest polygon wins where outlines overlap), and a new table is written.

The **Cell table** card in the **Transcripts** palette shows the active table and whether it is out of date — for example "12 cells added, 3 edited since this table was built" or "Up to date with the cell polygons." Use its refresh button to check for new edits.

To recompute:

1. In the **Cell table** card, click **Recompute counts…**
2. Enter a **Version label** (default "Recomputed")
3. Choose the scope:
   * **Edited cells only** — rebuilds only the cells that were added, edited or removed, plus their neighbors (molecules may have moved from one cell to the next). Every other row is carried over unchanged. This is much faster on large sections, and needs an existing table with something changed
   * **Every cell (full rebuild)** — reassigns every molecule from scratch
4. Optionally adjust the quality threshold (default 20) and **Only cells tagged** (default `cell`; leave blank to count every polygon)
5. Optionally tick **Also recompute PCA / UMAP / k-means**, which takes minutes on large sections
6. Click **Recompute**

Cell types carry over to the new table from each cell's tags.

{% hint style="info" %}
**When do I need a full rebuild?** An imported table can't tell which cells were edited — only which were added or removed — so recompute once to start tracking edits. Older tables without saved cell footprints also need one full rebuild before **Edited cells only** is available. An edited-cells rebuild also has to use the same quality threshold, tags and transcripts as the active table; if you change any of those, run a full rebuild.
{% endhint %}

### Switching between table versions

Recomputing never discards the previous table: it is kept as a version. Use the drop-down in the **Cell table** card to switch which table is active. Each entry shows its label and size (cells × genes). Switching re-points everything at the newly active table — live gene columns, filters, gates, plots, summaries and differential expression — and gates keep their shapes but are re-evaluated against the new values.

## Python API

The `nimbusimage` Python package exposes the same features through `ds.spatial`: the expression table, transcripts, table versions, neighborhoods and region summaries.

```python
ds.spatial.info()                                  # None when no table is registered
ds.spatial.features("cd", limit=10)                # search genes
ds.spatial.aggregate(["CD3E"], filters={"tags": {"values": ["B Cell"], "exclusive": False}})
ds.spatial.materialize(["CD3E", "MS4A1"], property_name="Gene Expression")
ds.spatial.virtual_path("CD3E")                    # ["spatial", "CD3E"], usable wherever a property path is
ds.spatial.score(symbols, name, method="mean")     # gene-set score
ds.spatial.differential(filters_a, filters_b=None, max_features=50)

ds.spatial.staleness()                             # cells added/edited/removed since the table
ds.spatial.recompute("v2", scope="dirty")          # re-count from the molecules; old table kept
ds.spatial.versions(); ds.spatial.activate_version(item_id)
ds.spatial.compute_neighborhood(radius_pixels=141) # 30 µm at 0.2125 µm/px
ds.spatial.region_summary("region", features=["CD3E"])
```

`aggregate` and `differential` take the same filter object the Objects tab uses, analysis gates included. The Xenium ingest steps are in `nimbusimage.xenium`; see the [API reference](https://arjunrajlaboratory.github.io/NimbusImage/) for details.

## Limitations and tips

* **No Transcripts or Add genes button?** The dataset has no registered transcripts or expression table. Ask whoever runs your server to run the ingest step.
* **"unknown feature"** means that gene isn't in this dataset's table — check the spelling, the `(protein)` suffix, or whether you switched datasets.
* **Live gene columns can't be sorted.** Use **Copy into a measurement** if you need to sort the object list by a gene.
* **H&E and morphology are separate images.** Use the objects and regions ingested onto the dataset you are viewing; don't import morphology-pixel files onto the H&E dataset or vice versa.
* **Distances or areas off by a constant factor?** Check the pixel size: click the scale bar in the viewer to open **Scale settings**. A pixel size typed by hand is never overwritten automatically.
* **Region counts look wrong?** Cells are counted by their center. Make sure every region carries the region tag and no cell does; "No polygon carries that tag" means the tag is misspelled or missing.
* **Image area black right after an ingest finishes?** Reload the page.
* **Recompute is 2D.** Molecules are assigned to cells in the image plane; z position is ignored.
* **Ask Nimbus AI.** The [Nimbus AI](../nimbus-ai.md) assistant knows how these tools work and can walk you through them.
