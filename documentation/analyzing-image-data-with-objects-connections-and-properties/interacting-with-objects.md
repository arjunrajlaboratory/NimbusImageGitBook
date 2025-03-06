# Interacting with objects

One of the main advantages of working in NimbusImage is the ability to directly interact with your objects. This interactive approach allows you to quickly refine your analysis by removing incorrect objects, adding missing ones, and organizing them with tags—all within the same interface.

## Selecting and manipulating objects

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption><p>Image with a bunch of green blob objects</p></figcaption></figure>

To interact with objects in your dataset:

* **Shift-drag** across objects to select multiple objects at once
* Once selected, a popup menu appears with several options:
  * **Delete selected** - Remove the selected objects
  * **Delete unselected** - Keep only the selected objects and remove all others
  * **Tag selected** - Add or change tags for the selected objects
  * **Color selected** - Apply custom colors to the selected objects
  * **Copy selected IDs** - Copy the object IDs to clipboard for reference

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption><p>Shift-drag allows you to select objects, revealing a popup menu to allow deletion, tagging, coloring, and identification by ID</p></figcaption></figure>

{% hint style="info" %}
The selection tool is particularly useful for cleaning up results from automated segmentation. You can quickly remove falsely identified objects or select groups of objects to apply a consistent tag.
{% endhint %}

## Object browser and filtering

The Object Browser provides powerful tools for managing which objects are visible in your view:

<figure><img src="../../.gitbook/assets/image (33).png" alt="" width="563"><figcaption><p>Object browser shows options for showing and hiding particular tags</p></figcaption></figure>

Key features include:

* **Tag filtering** - Filter objects by their tags (e.g., "nucleus" or "Brightfield blob")
* **Tag match options** - Choose if objects should match "Any" or "All" of the selected tags
* **Current frame only** - When enabled, shows only objects in the currently displayed time frame in the object list (helpful for time-lapse data)
* **Show annotations from hidden layers** - By default, annotations remain visible even when their corresponding layer is hidden; toggle this off to hide annotations when their layer is hidden

### Advanced filtering options

The Object Browser offers three powerful filtering mechanisms:

1. **Property value filter** - Filter objects based on measurements like area, intensity, or other computed properties
2. **Annotation ID filter** - Find specific objects by their unique IDs
3. **Region filter** - Draw a region of interest and show only objects within that area

These filters can be combined to precisely target objects meeting multiple criteria.

## Annotation list

The Annotation List provides a detailed tabular view of all objects in your dataset:

<figure><img src="../../.gitbook/assets/image (34).png" alt="" width="563"><figcaption><p>The annotation list shows all your objects</p></figcaption></figure>

The list offers several useful features:

* **Customizable columns** - Show or hide information like Annotation ID, Index, Shape, Tags, XY coordinates, Z position, and Time
* **Sorting** - Click any column header to sort by that property
* **Navigation** - Click on any row to navigate directly to that object in the image viewer
* **Bulk actions** - Select multiple objects using the checkboxes and perform actions like deletion or tagging
* **Pagination** - For datasets with many objects, navigate through pages with the pagination controls

## Working with properties

Properties allow you to measure features of your objects. These measurements can be displayed alongside your objects and used for filtering:

<figure><img src="../../.gitbook/assets/image (36).png" alt="" width="563"><figcaption><p>Properties panel showing available measurements for nucleus objects</p></figcaption></figure>

From the Properties panel, you can:

* **View available properties** - See what measurements are available for each object type
* **Show in list** - Select which properties should appear in the Annotation List
* **Use as filter** - Enable properties to be used for filtering in the Object Browser
* **Measure objects** - Create new properties by applying different measurement algorithms to your objects

{% hint style="info" %}
Press "t" while viewing your image to show property values directly on the objects themselves, making it easy to visualize measurements in context.
{% endhint %}
