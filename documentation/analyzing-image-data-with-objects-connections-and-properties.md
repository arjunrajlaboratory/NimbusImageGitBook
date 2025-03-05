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

Ultimately, most researchers want to extract numbers from their image data. These could correspond to fluorescent intensity across cells, or number of cells per colony, or density of filaments per region. NimbusImage allows you to make these computations easily by defining **properties**. A property (think: area) can be associated with an object and listed and exported for plotting and analysis. You can easily compute a lot of different properties using NimbusImage out of the box because of the flexibility that its tagging and connection system allows. For instance, if you want to find the count the number of spots connected to the basement membrane, that is easy to do with just a few clicks. To define a property, use this pane, choose the tag you wish to compute a property on, and then follow the prompts to create a property worker. Running the worker will compute the property over your entire dataset. These properties can also be listed in the Object Browser, making it easy to see what objects have what values for various properties.
