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

Learn more about these concepts in the following sections:

* [Tools for making objects](./tools-for-making-objects.md)
* [Tools for connecting objects](./tools-for-connecting-objects.md)
* [Measuring object properties](./measuring-object-properties.md)
