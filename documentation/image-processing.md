# Image processing

Images often can be improved through various image processing techniques. These are for things like background correction to remove uneven illumination, image registration to fix shaky timelapses, and enhance spots.

NimbusImage supports a number of these image processing techniques and we are planning to make more in the near future.

## Overall workflow

The image processing workflow in NimbusImage follows these steps:

1. **Select "ADD NEW TOOL"** from the Toolset panel
2. **Choose a processing tool** (such as "Crop")
3. **Configure the tool parameters** as needed
4. **Run the worker process** to apply the selected tool to your image
5. **Review results** a new dropdown appears just below the dataset navigator that allows you to switch between the orignal and processed images

<div align="left"><figure><img src="../.gitbook/assets/image (26).png" alt="" width="311"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../.gitbook/assets/image (27).png" alt="" width="314"><figcaption></figcaption></figure></div>

## Crop
