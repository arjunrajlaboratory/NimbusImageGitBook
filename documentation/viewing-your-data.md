# Viewing your image dataset

Once your images are loaded into NimbusImage, you can interact with it through the viewer. The viewer allows for easy navigation and flexible visualization.

**Key features include:**

* **Easy to use navigation and contrast settings**
* **"Unrolling" of variables** to show montages
*   **Overview "minimap".** Drag around the square to navigate; shift-click-drag to directly go to a location.

    <figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt="" width="156"><figcaption></figcaption></figure>
* **Dynamic scale bar.** Click the scale bar to adjust pixel sizes and other settings.
* **Zoom in and out of large images.** Scroll wheel zooms, just like Google Maps.
* **Flexible layer settings.** See below for more information about layers.

## Layers

Understanding layers can help unlock more flexibility in how you visualize your data. Generally, layers are most commonly thought of as mapping to channels, but in NimbusImage, they are capable of more. For instance, you can make multiple layers that draw from the same channel, but show different times in different colors, which can be very helpful for time lapse analysis.

<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption><p>Current time in green, next time in red so that you can see the shift</p></figcaption></figure>

### Layer grouping

Another useful feature is layer grouping, which allows you to put together multiple layers into a single grouped layer. For instance, if you have a couple fluorescence channels that you always want to show together, you can group them.

To use this feature, just drag the layers to a "drop zone" to combine:![](<../.gitbook/assets/image (8) (1) (1).png>)

You can add multiple layers to the group. Drag layers out of the group to undo the grouping.

## Label display options

NimbusImage allows you to customize how labels are displayed in your image viewer. You can toggle between:

* **Text labels**: Display descriptive labels such as "Well A1", "Position 3", etc.
* **Numeric identifiers**: Display simple numeric IDs for a cleaner view

This toggle helps you choose between more informative labels and a less cluttered display depending on your needs.

## Custom channel color preferences

You can set default channel color preferences in your user profile. These custom color settings:

* Automatically apply to new datasets you create or upload
* Can be overridden on a per-dataset basis if you want different colors for a specific dataset
* Help maintain consistency across your analyses

This feature is especially useful if you work with the same types of channels regularly and want them to always appear in your preferred colors.
