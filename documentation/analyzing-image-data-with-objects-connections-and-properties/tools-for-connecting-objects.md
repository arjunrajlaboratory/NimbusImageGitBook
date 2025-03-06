# Tools for connecting objects

In many cases, you may want to connect objects together, for instance, the same cell through a time lapse video, or spots to a nucleus. These connections can be made manually using connection tools such as Lasso connect or also automated connection algorithms such as Connect to Nearest. Connections can also be deleted manually. These connections can also sometimes be made when a property is computed to show you what objects were used in the computation.

## Best practices for connections

* **Use tags effectively**: Properly tagging your objects makes connection tools more precise
* **Assign hotkeys**: Set up hotkeys for your most frequently used connection tools
* **Think about directionality**: Remember that connections have direction (parent to child) which can be important for certain analyses

Connections form the foundation for many powerful analyses in NimbusImage, enabling you to quantify relationships between objects and trace structures across time.

## Manual connection tools: click and lasso connect

NimbusImage provides several intuitive tools for manually creating and removing connections between objects:

### Click connect

The **Click connect** tool allows you to create connections between objects by simply clicking them in sequence:

1. First, click on a "parent" object
2. Next, click on a "child" object
3. A connection will be established from the parent to the child

This tool is ideal for precisely connecting specific objects, like linking individual RNA spots to their corresponding cells or connecting organelles to their parent structures.

**Configuration options:**

* **Parent Annotation Tags**: Filter which types of objects can be selected as parents
* **Child Annotation Tags**: Filter which types of objects can be selected as children
* **Filter by layer**: Optionally restrict selections to objects on specific layers

### Lasso connect

The **Lasso connect** tool allows you to quickly connect multiple objects at once:

1. Draw a lasso around all the objects you want to connect
2. NimbusImage will automatically establish connections between the selected objects

This is particularly useful for:

* Connecting multiple spots to a cell at once
* Connecting sequential points in a time-lapse track
* Creating connections between groups of related objects

In time-lapse mode, the Lasso connect tool will intelligently connect objects sequentially by time point, making it extremely valuable for track creation and repair.

### Click disconnect

The **Click disconnect** tool allows you to remove individual connections:

1. Click on a connected parent object
2. Click on its connected child object
3. The connection between them will be removed

This is useful for removing incorrect connections without affecting other valid connections.

### Lasso disconnect

The **Lasso disconnect** tool allows you to quickly remove multiple connections at once:

1. Draw a lasso around the connected objects
2. All connections between objects within the lasso will be removed

This is particularly helpful when you need to clear all connections in a region and rebuild them correctly.

## Automated connection tools

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