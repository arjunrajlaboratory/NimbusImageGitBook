# Image processing

Images often can be improved through various image processing techniques. These are for things like background correction to remove uneven illumination, image registration to fix shaky timelapses, and enhance spots.

NimbusImage supports a number of these image processing techniques and we are planning to make more in the near future.

## Overall workflow

The image processing workflow in NimbusImage follows these steps:

1. **Select "ADD NEW TOOL"** from the Toolset panel
2. **Choose a processing tool** (such as "Crop") and create the tool
3. **Configure the tool parameters** as needed in the worker panel that appears after clicking on the tool
4. **Run the worker process** to apply the selected tool to your image
5. **Review results** a new dropdown appears just below the dataset navigator that allows you to switch between the orignal and processed images

<div align="left"><figure><img src="../.gitbook/assets/image (26).png" alt="" width="311"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../.gitbook/assets/image (27).png" alt="" width="314"><figcaption></figcaption></figure></div>

## Crop

The Crop tool allows you to reduce your image dimensions by selecting only a portion of the original image. This is useful for focusing on regions of interest, removing unnecessary image areas. You can both remove entire slices and also crop to particular regions.

### How to use

1. **Add the Crop tool** by clicking the "ADD NEW TOOL" button in the Toolset panel
2. **Configure crop parameters** using one of the following methods:
   - **XY Range**: Specify which XY positions to retain (especially useful for multi-position datasets)
   - **Z Range**: Specify which Z-slices to retain (for 3D images)
   - **Time Range**: Specify which time points to retain (for time-lapse sequences)
   - **Crop Rectangle**: Select a previously drawn rectangle or polygon annotation to define the crop region.
3. **Process the image** by running the worker
4. **Review the result** by switching between "Original image" and "cropped" in the dropdown menu

### Parameters

- **XY Range**: Enter position numbers to retain (format: "1-3, 5-8"). Default is all positions.
- **Z Range**: Enter Z-slice numbers to retain (format: "1-3, 5-8"). Default is all Z-slices.
- **Time Range**: Enter time point numbers to retain (format: "1-3, 5-8"). Default is all time points.
- **Crop Rectangle**: Select a tag that identifies a rectangle or polygon annotation to define the crop region.

### Technical details

The Crop tool works by creating a new image that contains only the specified region of interest from the original image. For annotation-based cropping, the tool uses the bounding box coordinates of the selected annotation to define the crop region. All metadata from the original image is preserved in the cropped output.

## Registration

The Registration tool corrects for movement and shift in time-lapse image sequences, helping to stabilize your data for more accurate analysis. This is particularly useful for long time-lapse experiments where sample drift occurs. It allows you to use both automated algorithms and manual control points to guide the registration process; you can even use both at the same time.

### How to use

1. **Add the Registration tool** by clicking the "ADD NEW TOOL" button in the Toolset panel
2. **Set the reference** parameters:
   - **Reference Z Coordinate**: Specify which Z-slice to use as reference
   - **Reference Time Coordinate**: Specify which time point to use as reference
   - **Reference Channel**: Select which channel to use for registration calculations
   - **Reference region tag**: Optionally restrict registration to a specific region of interest
   
3. **Select correction options**:
   - **Channels to correct**: Check which channels should be adjusted
   - **Control point tag**: Optionally use point annotations to guide registration
   - **Algorithm**: Choose the registration method that best suits your data

4. **Process the image** by running the worker
5. **Review the result** by switching between "Original image" and "registered" in the dropdown menu

### Parameters

- **Apply to XY coordinates**: Specify which XY positions to correct (format: "1-3, 5-8")
- **Reference Z Coordinate**: The Z-slice used as reference (default: 1)
- **Reference Time Coordinate**: The time point used as reference (default: 1)
- **Reference Channel**: Channel used for calculating registration
- **Channels to correct**: Select which channels to apply registration to
- **Reference region tag**: Optional tag for a region to use for registration calculations
- **Control point tag**: Optional tag for point annotations to use as registration anchors
- **Apply algorithm after control points**: When checked, applies the algorithm after control point corrections. For instance, you can use control points to roughly register your images and then use the algorithm to fine-tune the registration.
- **Algorithm**: Registration method to use (strongly recommended to use the default "Translation" algorithm):
  - **None (control points only)**: Uses only control points for registration
  - **Translation**: Corrects for X/Y movement (shifting)
  - **Rigid**: Corrects for translation and rotation
  - **Affine**: Corrects for translation, rotation, and scaling

### Technical details

The Registration tool calculates transformation matrices between time points using the StackReg algorithm from the PyStackReg library. For time-lapse sequences, each frame is aligned relative to the reference frame, creating a stable series where features remain in consistent positions.

The tool can use manual control points (annotated points that indicate the same feature across time points) to guide registration or can automatically detect and track features. When both are used, control points provide initial guidance followed by algorithmic refinement.

## Histogram Matching

The Histogram Matching tool normalizes intensity distributions across multiple images by matching their histograms to a reference image. This is particularly useful for correcting intensity variations in time-lapse sequences or multi-position acquisitions, ensuring consistent visualization and analysis.

### How to use

1. **Add the Histogram Matching tool** by clicking the "ADD NEW TOOL" button in the Toolset panel
2. **Set the reference image** by specifying:
   - **Reference XY Coordinate**: The position to use as reference
   - **Reference Z Coordinate**: The Z-slice to use as reference
   - **Reference Time Coordinate**: The time point to use as reference
3. **Select channels to correct** by checking the appropriate channel boxes
4. **Process the image** by running the worker
5. **Review the result** by switching between "Original image" and "normalized" in the dropdown menu

### Parameters

- **Reference XY Coordinate**: The XY position to use as intensity reference (default: 1)
- **Reference Z Coordinate**: The Z-slice to use as intensity reference (default: 1)
- **Reference Time Coordinate**: The time point to use as intensity reference (default: 1)
- **Channels to correct**: Select which channels should be histogram-matched

### Technical details

The Histogram Matching tool works by analyzing the intensity distribution of each specified channel in the reference image, then transforming the histograms of all other images to match that reference. This process preserves the relative differences in intensity within each image while making the overall intensity ranges consistent across the entire dataset.

This technique is especially valuable when:
- Comparing images acquired with different exposure settings
- Analyzing time-lapse data where photobleaching causes intensity decay over time
- Standardizing multi-position acquisitions with varying background intensities
- Preparing datasets for quantitative analysis that requires consistent intensity values

The implementation uses scikit-image's `match_histograms` function to perform precise histogram transformations while maintaining image details.

## Gaussian Blur

The Gaussian Blur tool smooths images by applying a Gaussian filter, which reduces noise and detail. This is useful for removing high-frequency noise, creating soft focus effects, or as a preprocessing step for other analysis techniques.

### How to use

1. **Add the Gaussian Blur tool** by clicking the "ADD NEW TOOL" button in the Toolset panel
2. **Configure the blur settings**:
   - **Sigma**: Control the blur strength (higher values create stronger blurring)
   - **Channel**: Select the default channel to blur
   - **All channels**: Check which channels should be processed
3. **Process the image** by running the worker
4. **Review the result** by switching between "Original image" and the blurred result in the dropdown menu

### Parameters

- **Sigma**: Determines the strength of the blur effect (range: 0-100, default: 20)
- **Channel**: The default channel to blur 
- **All channels**: Select multiple channels to apply blurring to

### Technical details

The Gaussian Blur tool applies a Gaussian filter to the selected channels of your image. This filter uses a Gaussian function (bell curve) to create a weighted average of each pixel's neighborhood. The sigma parameter controls the standard deviation of this Gaussian function - larger values consider pixels from a wider area, creating stronger blurring effects.

The implementation uses scikit-image's `filters.gaussian` function to perform the blurring operation. The tool preserves the original image's data type and dynamic range while applying the blur effect proportionally to the image's intensity values.

This technique is particularly useful for:
- Reducing random noise in images
- Softening edges and textures
- Preprocessing images before feature detection or segmentation
- Creating depth-of-field effects