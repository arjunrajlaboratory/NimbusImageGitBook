# Analyzing image data with objects, connections, and properties

## Overview

Analysis in NimbusImage is a little bit different than in other tools. The key concepts are _**Objects**_, _**Connections**_, and _**Properties**_. Throughout, the key organizational system is _**tagging**_, allowing flexible organization and more intuitive analysis patterns.

**Objects** are essentially annotations of items of interest within your dataset. Examples are:

1. Point objects representing spots of a particular RNA in the cytoplasm.
2. "Blob" objects representing the outline of a cell.
3. Line objects representing the basement membrane.

**Connections** between objects allow you to build relationships between objects. For instance, each RNA could be connected to a cell, meaning that that RNA is within that cell. Or a nucleolus object could be connected to a nucleus, or to a nearby paraspeckle. Connections allow you to document and analyze specific relationships, and interact with those relationships visually to get the analysis you want.

**Properties** are measurements you want to make on objects and connections for the final analysis of your data. For instance, average fluorescence intensity within the nucleus. Or distance from the speckle to the nuclear periphery. Or the length of a filament. Or the number of spots in the cytoplasm.

{% hint style="info" %}
**Tags are critical for organizing your analysis.** Objects should all have tags, which allow you to label, say, cells vs. nuclei, or spots for GAPDH mRNA or EEF2 mRNA. It helps you know what things represent.
{% endhint %}

NimbusImage is designed for scaling, so these tools will work for many thousands of objects.

## Example flows

_**The typical workflow in NimbusImage is to find objects in your images, either manually or using several automated tools and quantify properties of those objects.**_ Throughout, NimbusImage is designed to allow you to interact with your objects. You can manually add cells, remove incorrectly segmented nuclei, connect extra spots to a cell that got missed, and run your analysis on this corrected data. It is this flexibility that allows you to easily get numbers that accurately reflect your data.

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

## Finding objects

The way to create and edit objects is through the use of **tools**. Tools are defined by the user and are customized (via tags) to flexible organization of the results without a lot of clicking. There are two general categories of tools, manual and automated.

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

**Manual tools.** Manual tools are often based on a primitive type, like a point, line, or blob, and is customized with tags and other features. For instance, you might make a tool for circling cells in your image. You would choose a manual blob creation tool, name it "Nucleus" and add the tag \[nucleus]. You could also add a hotkey. That tool gets added to your interface and you can use it to circle cells at any time.

**Automated tools.** NimbusImage has been designed to allow the use of automated algorithms for finding things like cells and points in your images, often using the latest deep learning methods. For instance, you can set up an automated tool to use Cellpose to find cells within your images. These tools often have specific parameters that you can use to obtain optimal results.

### Manual blob/point/line/rectangle tools

Manual blob/point/line/rectangle tools are the most basic tools in NimbusImage. Set it up by clicking on "Add New Tool" and choosing "Manual Blob", "Manual Point", "Manual Line", or "Manual Rectangle". Set the tag, and then you can use it to create objects in your image. You can use the same tag for multiple tools. For instance, you can use an automated cell finding tool and then add more cells using the manual tool, and they will be all treated the same for downstream analysis.

### Segment-Anything semi-automated object finding, AKA "God Mode"

Segment-Anything is a new method for finding objects in images. It is a semi-automated tool that allows you to find objects in your images by either clicking on them or drawing a bounding box around them. To use it, click on "Add New Tool" and choose "ViT-B" under "Segment Anything Model". Options include:

* **Simplification**: The simplification parameter controls how much the segmentation is smoothed out. Smoother annotations are faster to run computations on and navigate.
* **Turbo mode**: The turbo mode allows you to rapidly segment without having to manually "accept" each segment.

Segment Anything works by first encoding the image to enable it to find the objects. This will take a few seconds to compute when you move to a new area. Every time you move the image, you will need to re-encode the image; if you want to avoid this, click the "lock" icon at the bottom left of the image to prevent the image from moving around.

Once encoded, just move your mouse over the image and it will outline what the object would be if you were to shift-click. Shift-click to make the object! Sometimes, it will give you better results if you define a box around the object you want to find. Just shift-click and drag to make a box, and it will segment that region.

{% hint style="info" %}
Segment Anything "sees" what you see in the image. Adjust the contrast and zoom to make objects visible and of a size that is around 5-15% of the size of the image for best results.
{% endhint %}

### Edit objects

You can edit objects by using the Annotation Edits -> Blob edit tool. With that tool, you can just drag on your object and it will "slice" it into a new object. Whatever line you draw will define a new outline for that segment of the object. That allows you to both remove and add areas to the objects without having to use separate brush and eraser tools.

### Automated object finding and connection

We have a number of automated tools for finding and connecting objects (cells, spots, etc.) that take advantage of the latest deep learning methods.

### Cellpose for automated cell finding

Cellpose is a deep learning-based tool for automatically finding and segmenting cells in microscopy images. It has been trained on a large collection of diverse cell images, making it highly effective for many cell types without requiring additional training. Cellpose is a powerful starting point for cell segmentation, allowing you to quickly generate cell outlines that can be refined with NimbusImage's interactive tools.

{% hint style="info" %}
Note that NimbusImage also allows for retraining of the Cellpose models to (often greatly) enhance performance for your specific dataset.
{% endhint %}

#### Available models

NimbusImage includes several pre-trained Cellpose models:

* **cyto3**: The most accurate for general cell segmentation (recommended default)
* **cyto2**: An older model for cell segmentation
* **cyto**: The original cell segmentation model
* **nuclei**: Specifically trained for nuclear segmentation

#### Key parameters

* **Primary Channel**: The main channel to use for segmentation
  * For cytoplasm segmentation (Cyto3): use your cytoplasm/membrane channel
  * For nuclear segmentation (Nuclei): use your nuclear stain channel (e.g., DAPI)
* **Secondary Channel** (optional): A secondary channel to improve segmentation
  * For cytoplasm segmentation (Cyto3): you can add your nuclear channel
  * For nuclear segmentation (Nuclei): leave this blank (adding a secondary channel may decrease performance)
* **Diameter**: The approximate diameter of cells in pixels
  * **This parameter is crucial for good results**
  * Set this as close as possible to the actual cell diameter in your images
* **Smoothing**: Controls how much the cell outlines are simplified (0-10)
  * Higher values create smoother outlines with fewer vertices
  * Default of 0.7 works well for most images
  * Increase for smoother boundaries, decrease for more precise outlines
  * Very precise outlines can decrease performance, especially if you have a large number of objects
* **Padding**: Expand or contract the final cell outlines in pixels
  * Positive values expand the outlines (useful if cells appear too small)
  * Negative values contract the outlines (useful if segmentation is too generous)
  * Default of 0 means no adjustment

#### Advanced parameters for large images

* **Tile Size**: The size of each image tile in pixels
  * Default of 1024 works well for most images
  * Decrease if you encounter errors
  * Larger tiles will require more memory and can cause Cellpose to crash
* **Tile Overlap**: The fraction of overlap between adjacent tiles
  * Default of 0.1 (10% overlap) works well in most cases
  * **Important**: Make sure your overlap is larger than your largest cells
  * For example, for 1024 pixel tiles with 0.1 overlap, the largest cell should be less than 102 pixels across

#### Best practices

1. **Start with the right model**: Use cyto3 for general cell segmentation or nuclei for nuclear segmentation, or use your own custom retrained model
2. **Set the diameter carefully**: This is the most important parameter for accurate results
3. **Check results visually**: Always inspect the segmentation and refine parameters if needed
4. **Use the secondary channel** when segmenting cytoplasm if you have a good nuclear stain
5. **Post-process as needed**: Use NimbusImage's manual editing tools to correct any segmentation errors

### Cellpose Training

NimbusImage offers the ability to train custom Cellpose models directly within the platform using your own annotated data. This feature allows you to create specialized segmentation models tailored to your specific cell types or imaging conditions. Custom models will often provide greatly improved performance for your specific dataset, even if your cells look pretty "normal", and especially if they don't!

#### Training data preparation

To train a custom model, you'll need:

1. Representative images with cells you want to segment
2. Accurate cell annotations (outlines) created manually or corrected from automated results
3. Optional: Defined regions of interest for training

#### Key parameters

* **Base Model**: The pre-trained model to use as a starting point
  * **cyto3**: Recommended for most cell types
  * **nuclei**: Use when training a nuclear segmentation model
  * **Custom models**: Previously trained models will also appear here
* **Nuclear Model?**: Check this box if you're training a model for nuclear segmentation
  * When checked, the model will be optimized for nuclear detection
* **Output Model Name**: Name for your custom model
  * This model will be saved and appear in the Cellpose worker's model list
* **Primary Channel**: The main channel for segmentation
  * For cytoplasm models: use your cytoplasm/membrane channel
  * For nuclear models: use your nuclear stain channel
* **Secondary Channel**: The secondary channel to improve segmentation
  * For cytoplasm models: your nuclear channel
  * For nuclear models: leave blank or set to -1
* **Training Tag**: The tag applied to annotated cells used for training
  * All cells with this tag will be used to train the model
  * Use this to select high-quality annotations
* **Training Region**: Optional tag (recommended) to define specific regions for training
  * If selected, only annotations within these regions will be used
  * Useful for limiting training to representative areas of your image

#### Training parameters

Unless you have a specific reason to change these, leave them at the default values.

* **Learning Rate**: Controls how quickly the model adapts during training
  * Default: 0.01
  * Lower values (0.001) create more stable but slower training
  * Higher values can speed up training but might decrease stability
* **Epochs**: Number of training iterations
  * Default: 1000
  * More epochs generally improve results but take longer
  * Consider increasing for complex cell types
* **Weight Decay**: Regularization parameter to prevent overfitting
  * Default: 0.0001
  * Higher values create simpler models that may generalize better

#### Training workflow

1. Create high-quality annotations of your cells
   * Tag these annotations with a consistent label (e.g., "training\_cells")
   * Ensure annotations are accurate and representative
   * **Don't forget that what you do NOT annotate will also be used for training!**
2. Optional: Define training regions
   * Create rectangles or polygons around areas with good examples
   * Tag these regions (e.g., "training\_region")
   * **Choosing specific regions can be very helpful in focusing the retraining on specific areas of your image**
3. Add a Cellpose Training tool from the toolset menu
   * Configure all parameters as described above
   * Run the training process
4. Use your custom model
   * After training completes, your model will appear in the Cellpose worker's model list
   * Select it when using the regular Cellpose tool for segmentation

#### Tips for successful training

1. **Provide diverse examples**: Include cells of different sizes, shapes, and intensities
2. **Quality over quantity**: A smaller set of perfect annotations is better than many poor ones. A few good images, carefully annotated, will usually do the trick.
3. **Choose representative regions**: Select areas with good imaging quality and typical cells. Be sure to include examples of cells that the default algorithm might have trouble with.
4. **Be patient**: Training can take several minutes to complete

#### Advanced usage

Your custom Cellpose models are saved in a `.cellpose` directory. You can:

* Manually add models trained offline to this directory
* Share models between team members by copying model files
* Use these models in the standard Cellpose Python package

The integration between NimbusImage and Cellpose makes it easy to create specialized models for your specific research needs without requiring deep learning expertise.

### Piscis for automated spot finding

Piscis is a deep learning-based tool for automatically finding and segmenting spots in microscopy images. It has been trained on a large collection of diverse spot images, making it highly effective for many spot types without requiring additional training. Piscis is a powerful starting point for spot segmentation, allowing you to quickly generate spot outlines that can be refined with NimbusImage's interactive tools. It can be retrained on your own data as well, which can often give you great results if the default models don't work well for your data.

> **Key tip**: If you're getting too many or too few spots, try different models first before adjusting other parameters. The built-in models vary in sensitivity, and selecting the right one is usually more effective than tweaking threshold values.

#### How Piscis works

Piscis uses a specialized neural network designed specifically for detecting small punctate structures in fluorescence microscopy images, such as:

* RNA molecules in FISH experiments
* Protein clusters
* Vesicles
* Small organelles
* Synaptic puncta

The model can work in both 2D (single slice) and 3D (Z-stack) modes, making it flexible for different experimental setups.

#### Key parameters

* **Model**: Select which pre-trained Piscis model to use
  * Different models have varying levels of sensitivity
  * Try several models if you're not getting optimal results
  * Custom trained models will also appear in this list
* **Mode**: Choose between "Current Z" or "Z-Stack"
  * **Current Z**: Process each Z-slice independently (2D mode)
  * **Z-Stack**: Process the entire Z-stack as a 3D volume (better for connecting spots across Z)
* **Scale**: Adjust for the size of spots (0-5)
  * Default value of 1 works well for most applications
  * Increase to detect larger spots
  * Decrease to detect smaller spots
  * Affects how the model interprets spot size relative to the training data
* **Threshold**: Confidence threshold for spot detection (0-9)
  * Default value of 1.0 works for most cases
  * Note that this parameter has a relatively minor effect compared to changing models
  * Higher values create stricter detection (fewer spots)
  * Lower values create more lenient detection (more spots)
* **Skip Frames Without**: Optional tag to skip processing frames
  * If specified, only process frames containing objects with the given tag
  * Useful for optimizing processing time by focusing on relevant frames

#### Advanced features

* **Batch processing**: Process multiple positions, Z-slices, or time points
  * Use the "Batch XY", "Batch Z", and "Batch Time" fields to specify ranges
  * Format example: "1-3, 5-8" processes positions 1, 2, 3, 5, 6, 7, 8
  * Note: If using "Z-Stack" mode, the "Batch Z" field is ignored

#### Best practices

1. **Start with the default model**: Try the default "20230905" model first
2. **Try different models**: If detection isn't optimal, switching models is more effective than adjusting thresholds
3. **Use Z-Stack mode** for 3D data where spots may span multiple Z-slices
4. **Validate results visually**: Always check the detection results manually
5. **Consider retraining**: For specialized applications, retraining on your own data can significantly improve results

#### Example workflow

1. Add a new Piscis tool from the toolset menu
2. Select your channel containing spots
3. Choose a model (start with the default)
4. Select either "Current Z" or "Z-Stack" mode
5. Run the model
6. Review the results
7. If needed, try a different model or adjust parameters and run again

#### Training custom models

If the pre-built models don't work well for your specific spot detection needs, consider training a custom model using the Piscis Train tool (documented separately). Custom-trained models will appear in the model selection dropdown once trained.

Piscis is particularly effective for RNA FISH and similar applications where automatic detection of small punctate structures is needed, saving significant time compared to manual annotation.

### Piscis Training

The Piscis Training tool allows you to create custom spot detection models tailored to your specific microscopy data. By training on your own annotated examples, you can significantly improve spot detection performance for challenging or unique datasets.

> **Key tip**: You don't need extensive training data to get good results! Even a few carefully annotated regions can produce a highly effective custom model.

#### Why train a custom model?

Consider training a custom Piscis model when:

* Default models consistently detect too many or too few spots
* Your spots have unusual characteristics (size, intensity, shape)
* You're working with specialized microscopy techniques
* Background noise or artifacts are causing detection issues

#### Training data preparation

To train an effective custom model:

1. **Create point annotations** for the spots you want to detect
   * Tag them consistently (e.g., "training\_spots")
   * Be thorough within your selected regions - mark all visible spots
2. **Define training regions** where your annotations are complete
   * Use rectangles or polygons to outline areas with fully annotated spots
   * Tag these regions consistently (e.g., "training\_region")
   * Focus on high-quality regions rather than quantity

#### Key parameters

* **Initial Model Name**: The base model to start training from
  * Starting from an existing model (like "20230905") speeds up training
  * The base model provides initial weights that get refined with your data
* **New Model Name**: What to call your custom model
  * Default is a timestamp (e.g., "20250305\_143022")
  * Consider using a descriptive name for your experiment or spot type
* **Annotation Tag**: The tag used on your spot annotations
  * Only points with this tag will be used for training
* **Region Tag**: The tag used on your training regions
  * Only annotations within these regions will be used for training
  * Crucial for ensuring the model learns from fully annotated areas

#### Training parameters

* **Learning Rate**: Controls how quickly the model adapts (default: 0.2)
  * Higher values can lead to faster convergence but may be less stable
  * Lower values produce more stable but slower training
* **Weight Decay**: Regularization parameter to prevent overfitting (default: 0.0001)
  * Higher values create simpler models that may generalize better
* **Epochs**: Number of training iterations (default: 40)
  * More epochs generally improve results but take longer
  * The default is usually sufficient for good performance
* **Random Seed**: Controls randomness in training for reproducibility (default: 42)
  * Change this value if you want to try different random initializations

#### Training workflow

1. **Create point annotations**
   * Manually mark spots in representative areas of your image
   * Apply a consistent tag (e.g., "training\_points")
2. **Define training regions**
   * Draw rectangles or polygons around fully annotated areas
   * Apply a consistent tag (e.g., "training\_region")
3. **Configure the Piscis Train tool**
   * Select a base model
   * Configure training parameters (or use defaults)
   * Specify your annotation and region tags
4. **Run the training process**
   * This will take several minutes depending on your data
   * The model will be saved with your specified name
5. **Use your custom model**
   * Your trained model will automatically appear in the Piscis tool's model list
   * Select it when using Piscis for spot detection

#### Best practices

1. **Quality over quantity**: A few well-annotated regions are better than many poorly annotated ones
2. **Include challenging examples**: Include difficult spots in your training data
3. **Use representative regions**: Select areas that reflect the variability in your dataset
4. **Start small**: Begin with a small training set and evaluate before expanding
5. **Iterative improvement**: Train, test, correct annotations, and train again for best results

#### Testing your model

After training, test your model by:

1. Using the standard Piscis tool with your new model
2. Comparing results against manual annotations in regions not used for training
3. Adjusting the Scale parameter slightly if needed for fine-tuning

Custom-trained Piscis models often dramatically improve spot detection accuracy for specialized applications, saving significant time in your image analysis workflow.

## Connecting objects

In many cases, you may want to connect objects together, for instance, the same cell through a time lapse video, or spots to a nucleus. These connections can be made manually using connection tools such as Lasso connect or also automated connection algorithms such as Connect to Nearest. Connections can also be deleted manually. These connections can also sometimes be made when a property is computed to show you what objects were used in the computation.

### Best practices for connections

* **Use tags effectively**: Properly tagging your objects makes connection tools more precise
* **Assign hotkeys**: Set up hotkeys for your most frequently used connection tools
* **Think about directionality**: Remember that connections have direction (parent to child) which can be important for certain analyses

Connections form the foundation for many powerful analyses in NimbusImage, enabling you to quantify relationships between objects and trace structures across time.

### Manual connection tools: click and lasso connect

NimbusImage provides several intuitive tools for manually creating and removing connections between objects:

#### Click connect

The **Click connect** tool allows you to create connections between objects by simply clicking them in sequence:

1. First, click on a "parent" object
2. Next, click on a "child" object
3. A connection will be established from the parent to the child

This tool is ideal for precisely connecting specific objects, like linking individual RNA spots to their corresponding cells or connecting organelles to their parent structures.

**Configuration options:**

* **Parent Annotation Tags**: Filter which types of objects can be selected as parents
* **Child Annotation Tags**: Filter which types of objects can be selected as children
* **Filter by layer**: Optionally restrict selections to objects on specific layers

#### Lasso connect

The **Lasso connect** tool allows you to quickly connect multiple objects at once:

1. Draw a lasso around all the objects you want to connect
2. NimbusImage will automatically establish connections between the selected objects

This is particularly useful for:

* Connecting multiple spots to a cell at once
* Connecting sequential points in a time-lapse track
* Creating connections between groups of related objects

In time-lapse mode, the Lasso connect tool will intelligently connect objects sequentially by time point, making it extremely valuable for track creation and repair.

#### Click disconnect

The **Click disconnect** tool allows you to remove individual connections:

1. Click on a connected parent object
2. Click on its connected child object
3. The connection between them will be removed

This is useful for removing incorrect connections without affecting other valid connections.

#### Lasso disconnect

The **Lasso disconnect** tool allows you to quickly remove multiple connections at once:

1. Draw a lasso around the connected objects
2. All connections between objects within the lasso will be removed

This is particularly helpful when you need to clear all connections in a region and rebuild them correctly.

### Automated connection tools

NimbusImage provides powerful automated tools that can establish connections between objects based on various criteria, saving you considerable time compared to manual connections.

### Connect to nearest

The **Connect to nearest** tool automatically connects objects based on spatial proximity:

1. Each object with the "parent" tag will be connected to its nearest object(s) with the "child" tag
2. The connections are established based on configurable distance and relationship criteria

**Configuration options:**

* **Parent tag**: Tag that identifies which objects will serve as parents in the connections
* **Child tag**: Tag that identifies which objects will serve as children in the connections
* **Connect across Z**: When enabled, allows connections between objects on different Z-slices
* **Connect across T**: When enabled, allows connections between objects at different time points
* **Connect to closest centroid or edge**: Choose whether to measure distance from:
  * **Centroid**: The central point of each object (faster, simpler)
  * **Edge**: The boundary of each object (more precise for irregularly shaped objects)
* **Restrict connection**: Apply additional constraints to connections:
  * **None**: Connect based solely on distance
  * **Touching parent**: Only connect children that physically touch their parent
  * **Within parent**: Only connect children that are completely contained within their parent
* **Max distance (pixels)**: The maximum allowed distance between parent and child objects
* **Connect up to N children**: Limit the number of children that can connect to each parent

This tool is particularly useful for:

* Connecting RNA spots to their nearest nucleus
* Assigning cells to their closest blood vessel
* Connecting subcellular structures to their parent cells
* Efficiently processing large datasets with many objects

Let me update the documentation section on the "Connect timelapse" tool with more detailed information based on the code you've provided:

### Connect timelapse

The **Connect timelapse** tool specializes in automatically tracking objects across sequential time points:

1. Objects with the same tag are connected from one time frame to the next
2. Connections are established based on spatial proximity between frames
3. The algorithm intelligently handles object movement between frames

This is especially valuable for cell tracking, particle movement analysis, and other time-dependent studies.

**Configuration options:**

* **Object to connect tag**: Specifies which objects to track across time points (all objects with this tag will be connected)
* **Connect across gaps**: Allows connecting objects even when there are missing time points
  * Set a value from 0-10 to determine how many time points can be skipped
  * For example, a value of 1 would connect an object at t=5 directly to t=7 if t=6 is missing
* **Max distance**: The maximum pixel distance objects can move between frames and still be considered the same object
  * Set this based on how much your objects typically move between frames
  * Lower values (5-20 pixels) work well for slow-moving objects
  * Higher values may be needed for rapidly moving objects or lower frame rates

**How it works:**

1. The algorithm processes each spatial location (XY, Z) separately
2. For each time point, it searches for the closest matching objects in subsequent time points
3. Connections are created from later time points to earlier ones (children to parents)
4. All connections are automatically tagged with "Time lapse connection" for easy identification

This tool is perfect for:

* Automatically generating cell lineage trees
* Tracking particle movement over time
* Analyzing cell migration patterns
* Measuring growth or movement rates

**Best practices:**

* Start with a small max distance (10-20 pixels) and increase if needed
* Use the "Connect across gaps" feature when you have intermittently missing objects. These can be later fixed manually using [Time lapse mode](../documentation/time-lapse-mode.md)
* When tracking dividing cells, use this tool first, then manually correct division events
* Review tracks in Time lapse mode to identify and fix any tracking errors
* For very dense or challenging datasets, consider tracking a subset of objects first

After running the Connect timelapse tool, you can use the Time lapse mode (discussed in the [Time lapse mode](../documentation/time-lapse-mode.md) section) to visualize, review, and manually correct the resulting tracks.

## Quantifying properties

Ultimately, most researchers want to extract numbers from their image data. These could correspond to fluorescent intensity across cells, or number of cells per colony, or density of filaments per region. NimbusImage allows you to make these computations easily by defining **properties**. A property (think: area) can be associated with an object and listed and exported for plotting and analysis. You can easily compute a lot of different properties using NimbusImage out of the box because of the flexibility that its tagging and connection system allows. For instance, if you want to find the count the number of spots connected to the basement membrane, that is easy to do with just a few clicks.

First, click on Object List, then, in "Properties", click the blue "Measure Objects" button:

<div align="left"><figure><img src="../../.gitbook/assets/image.png" alt="" width="563"><figcaption></figcaption></figure></div>

That brings up the Property window:

<div align="left"><figure><img src="../../.gitbook/assets/image (1).png" alt="" width="375"><figcaption></figcaption></figure></div>

Choose the tag of the object you want to quantify:

<div align="left"><figure><img src="../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure></div>

Then choose the Algorithm, like "Blob metrics". It will bring up a list of options:

<div align="left"><figure><img src="../../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure></div>

Click "Create Property" and it will create and run the property worker. When done, it will look like this:

<div align="left"><figure><img src="../../.gitbook/assets/image (5).png" alt="" width="375"><figcaption></figcaption></figure></div>

When you close the Property panel, it will open up the Properties pane. Click on "nucleus Blob metrics", then click on the Area checkbox:

<div align="left"><figure><img src="../../.gitbook/assets/image (7).png" alt="" width="375"><figcaption></figcaption></figure></div>

Now your property will show up in the property list:

<div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt="" width="375"><figcaption></figcaption></figure></div>

If you push "t", it will show the values in the image itself:

<div align="left"><figure><img src="../../.gitbook/assets/image (9).png" alt="" width="375"><figcaption><p>After pushing "t", you can see the values on the image itself</p></figcaption></figure></div>

These values can be exported into a CSV under "Objects" -> Actions -> Export CSV

<div align="left"><figure><img src="../../.gitbook/assets/image (12).png" alt="" width="375"><figcaption></figcaption></figure></div>

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
