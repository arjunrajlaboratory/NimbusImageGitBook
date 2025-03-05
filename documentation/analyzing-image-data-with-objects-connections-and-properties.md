# Analyzing image data with objects, connections, and properties

## Overview

Analysis in NimbusImage is a little bit different than in other tools. The key concepts are _**Objects**_, _**Connections**_, and _**Properties**_. Throughout, the key organizational system is _**tagging**_, allowing flexible organization and more intuitive analysis patterns.

NimbusImage is designed for scaling, so these tools will work for many thousands of objects.

## Example flows

Here's a couple examples of a workflow to make these concepts more concrete.

### Measure cell areas:

1. Circle a bunch of cells, tag them with <kbd><mark style="background-color:orange;">fibroblast<mark style="background-color:orange;"></kbd>.
2. Create a "metrics" property and compute it.
3. List the areas for each.

### Count dots in each cell

1. Circle cells ( <kbd><mark style="background-color:orange;">fibroblast<mark style="background-color:orange;"></kbd>) and click on dots ( <kbd><mark style="background-color:orange;">UBC mRNA<mark style="background-color:orange;"></kbd>)
   1. More likely, you will use automated tools in NimbusImage to find cells and dots.
2. Use a "Connect to nearest" tool to automatically connect each dot to a cell.
3. Create a property to count the number of UBC mRNA spots connected to fibroblasts.
4. List the point count for each cell.

### Track cells over time

1. Find cells ( <kbd><mark style="background-color:orange;">HEK<mark style="background-color:orange;"></kbd>). NimbusImage has many automated tools for time lapse analysis specifically.
2. Use a "Connect timelapse" tool to automatically connect cells over time.
3. Use "Time lapse mode" to review and correct tracks.
4. Create a property to store all the tree information.
5. Export the tree information in a CSV for downstream analysis in Python/R.

## Definitions: objects, connections, properties

### Objects

Objects are essentially annotations of items of interest within your dataset. Examples are:

1. Point objects representing spots of a particular RNA in the cytoplasm.
2. "Blob" objects representing the outline of a cell.
3. Line objects representing the basement membrane.

### Connections

Connections between objects allow you to build relationships between objects. For instance, each RNA could be connected to a cell, meaning that that RNA is within that cell. Or a nucleolus object could be connected to a nucleus, or to a nearby paraspeckle. Connections allow you to document and analyze specific relationships, and interact with those relationships visually to get the analysis you want.

### Properties

Properties are measurements you want to make on objects and connections for the final analysis of your data. For instance, average fluorescence intensity within the nucleus. Or distance from the speckle to the nuclear periphery. Or the length of a filament. Or the number of spots in the cytoplasm.

{% hint style="info" %}
Tags are critical for organizing your analysis. Objects should all have tags, which allow you to distinguish between, say, blobs that represent mouse vs. human cells.
{% endhint %}

_The typical workflow in NimbusImage is to find objects in your images, either manually or using several automated tools, connect those objects as desired, and quantify properties of those objects._ Throughout, NimbusImage is designed to allow you to interact with your objects. You can manually add cells, remove incorrectly segmented nuclei, connect extra spots to a cell that got missed, and run your analysis on this corrected data. It is this flexibility that allows you to easily get numbers that accurately reflect your data without having to live with the results of a faulty pipeline.

## Finding objects

The way to create and edit objects is through the use of **tools**. Tools are defined by the user and are customized (via tags) to flexible organization of the results without a lot of clicking. There are two general categories of tools, manual and automated.

**Manual tools.** Manual tools are often based on a primitive type, like a point, line, or blob, and is customized with tags and other features. For instance, you might make a tool for circling cells in your image. You would choose a manual blob creation tool, name it "Nucleus" and add the tag \[nucleus]. You could also add a hotkey. That tool gets added to your interface and you can use it to circle cells at any time.

**Automated tools.** NimbusImage has been designed to allow the use of automated algorithms for finding things like cells and points in your images, often using the latest deep learning methods. For instance, you can set up an automated tool to use Cellpose to find cells within your images. These tools often have specific parameters that you can use to obtain optimal results.

## Connecting objects

In many cases, you may want to connect objects together, for instance, the same cell through a time lapse video, or spots to a nucleus. These connections can be made manually using connection tools such as Lasso connect or also automated connection algorithms such as Connect to Nearest. Connections can also be deleted manually. These connections can also sometimes be made when a property is computed to show you what objects were used in the computation.

## Quantifying properties

Ultimately, most researchers want to extract numbers from their image data. These could correspond to fluorescent intensity across cells, or number of cells per colony, or density of filaments per region. NimbusImage allows you to make these computations easily by defining **properties**. A property (think: area) can be associated with an object and listed and exported for plotting and analysis. You can easily compute a lot of different properties using NimbusImage out of the box because of the flexibility that its tagging and connection system allows. For instance, if you want to find the count the number of spots connected to the basement membrane, that is easy to do with just a few clicks.

First, click on Object List, then, in "Properties", click the blue "Measure Objects" button:

<div align="left"><figure><img src="../.gitbook/assets/image.png" alt="" width="563"><figcaption></figcaption></figure></div>

That brings up the Property window:

<div align="left"><figure><img src="../.gitbook/assets/image (1).png" alt="" width="375"><figcaption></figcaption></figure></div>

Choose the tag of the object you want to quantify:

<div align="left"><figure><img src="../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure></div>

Then choose the Algorithm, like "Blob metrics". It will bring up a list of options:

<div align="left"><figure><img src="../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure></div>

Click "Create Property" and it will create and run the property worker. When done, it will look like this:

<div align="left"><figure><img src="../.gitbook/assets/image (5).png" alt="" width="375"><figcaption></figcaption></figure></div>

When you close the Property panel, it will open up the Properties pane. Click on "nucleus Blob metrics", then click on the Area checkbox:

<div align="left"><figure><img src="../.gitbook/assets/image (7).png" alt="" width="375"><figcaption></figcaption></figure></div>

Now your property will show up in the property list:

<div align="left"><figure><img src="../.gitbook/assets/image (8).png" alt="" width="375"><figcaption></figcaption></figure></div>

If you push "t", it will show the values in the image itself:

<div align="left"><figure><img src="../.gitbook/assets/image (9).png" alt="" width="375"><figcaption><p>After pushing "t", you can see the values on the image itself</p></figcaption></figure></div>

These values can be exported into a CSV under "Objects" -> Actions -> Export CSV

<div align="left"><figure><img src="../.gitbook/assets/image (12).png" alt="" width="375"><figcaption></figcaption></figure></div>

### Blob metrics (area, perimeter, etc.)

The Blob Metrics property worker calculates a comprehensive set of morphological measurements for blob-shaped (polygon) objects in your dataset. This is particularly useful for analyzing cell shapes, nuclei, or any other blob-like structures you've annotated.

#### Available metrics:

* **Area**: The total area enclosed by the object (in square pixels or physical units)
* **Perimeter**: The length of the object's boundary (in pixels or physical units)
* **Centroid**: The geometric center (x,y coordinates) of the object
* **Elongation**: Measures how stretched out the object is (value between 0-1, where 1 is maximally elongated)
* **Convexity**: Ratio of the object's area to the area of its convex hull (measures how convex vs. concave the shape is)
* **Solidity**: Ratio of the object's perimeter to the perimeter of its convex hull
* **Rectangularity**: How well the object fits within its minimum bounding rectangle
* **Circularity**: How closely the object resembles a perfect circle (4π × Area/Perimeter²)
* **Eccentricity**: Measures how much the object deviates from being circular (value between 0-1, where 0 is a circle)

#### How to use:

1. Create blob objects in your image (manually or using automated tools)
2. Tag these objects appropriately (e.g., `nucleus`, `cell`, etc.)
3. Create a new property using the Blob Metrics worker
4. Select which tags to analyze
5. Choose whether to use physical units (μm, mm, etc.) or pixel units
6. Run the property worker to calculate metrics for all matching objects

#### Physical units:

When the "Use physical units" option is enabled, all measurements will be converted from pixels to the selected physical unit (μm, mm, m, or nm) based on the pixel size metadata in your image. This allows for consistent measurements across datasets with different magnifications or resolutions.

This property is useful for:

* Measuring and comparing cell or organelle sizes
* Analyzing shape changes in response to treatments
* Quantifying morphological differences between cell types
* Correlating shape features with biological function

### Best practices for intensity measurements:

1. **Background correction**: Consider using background subtraction before measuring intensities for more accurate results
2. **Consistent exposure**: For comparative studies, ensure all images were acquired with the same exposure settings
3. **Channel selection**: Carefully select which channel to measure based on your experimental design
4. **Annulus size**: When using annular measurements, adjust the radius to match the biological structure you're analyzing (e.g., typical cytoplasm width)
5. **Validation**: Visually verify that your measurements align with the visible intensity patterns in your images

### Blob Intensity

The Blob Intensity property worker calculates pixel intensity statistics inside blob-shaped (polygon) objects in your dataset. This is ideal for measuring fluorescence within cells, nuclei, or other structures you've annotated.

#### Available metrics:

* **Mean Intensity**: The average pixel intensity within the object
* **Max Intensity**: The brightest pixel value within the object
* **Min Intensity**: The dimmest pixel value within the object
* **Median Intensity**: The median pixel value (50th percentile)
* **25th Percentile Intensity**: The intensity value below which 25% of pixels fall
* **75th Percentile Intensity**: The intensity value below which 75% of pixels fall
* **Total Intensity**: The sum of all pixel intensities within the object

#### How to use:

1. Create blob objects in your image (manually or using automated tools)
2. Tag these objects appropriately (e.g., `nucleus`, `cell`, etc.)
3. Create a new property using the Blob Intensity worker
4. Select the channel you want to measure intensity from (this can be different from the layer where annotations are drawn)
5. Run the property worker to calculate intensity metrics for all matching objects

#### Applications:

* Quantifying protein expression levels within cells
* Measuring nuclear vs. cytoplasmic signal ratios
* Comparing fluorescence intensities between experimental conditions
* Identifying cells with high or low expression of a marker

### Blob Intensity Percentile

This worker extends the basic intensity analysis by allowing you to specify exactly which percentile to measure, giving you more flexibility for your specific analysis needs.

#### Parameters:

* **Channel**: The image channel to measure intensity from. Note that this can be different from the channel where annotations are drawn. So you can calculate, e.g., the RFP intensity in objects defined by the DAPI channel to calculate nuclear RFP intensity.
* **Percentile**: A value between 0 and 99.99999 to specify which percentile intensity to calculate (default: 50)

#### Output:

* **Nth Percentile Intensity**: The intensity value at your specified percentile

#### When to use:

* When you need to focus on a specific portion of the intensity distribution
* For filtering out outliers (using high or low percentiles)
* When the median (50th percentile) doesn't fully capture the intensity characteristics you're interested in

### Blob Annulus Intensity

The Blob Annulus Intensity worker measures pixel intensity in a ring-shaped region around each blob object. This is particularly valuable for quantifying cytoplasmic signals around nuclei or membrane markers surrounding cells.

#### Parameters:

* **Channel**: The image channel to measure intensity from
* **Radius**: The width of the annular region in pixels (default: 10)

#### Available metrics:

* **Mean Intensity**: The average pixel intensity within the annular region
* **Max Intensity**: The brightest pixel value within the annular region
* **Min Intensity**: The dimmest pixel value within the annular region
* **Median Intensity**: The median pixel value in the annular region
* **25th Percentile Intensity**: The intensity value below which 25% of pixels fall
* **75th Percentile Intensity**: The intensity value below which 75% of pixels fall
* **Total Intensity**: The sum of all pixel intensities within the annular region

#### Applications:

* Measuring cytoplasmic fluorescence around nuclear objects
* Quantifying membrane-associated markers surrounding cells
* Analyzing protein localization patterns at cell boundaries
* Studying gradient distributions of signals around organelles

### Blob Annulus Intensity Percentile

This worker combines the flexibility of percentile selection with annular region measurement, allowing for precise control over which statistical metric to use in your ring-shaped regions of interest.

#### Parameters:

* **Channel**: The image channel to measure intensity from
* **Radius**: The width of the annular region in pixels (default: 10)
* **Percentile**: A value between 0 and 99.99999 to specify which percentile intensity to calculate (default: 50)

#### Output:

* **Nth Percentile Intensity**: The intensity value at your specified percentile within the annular region
