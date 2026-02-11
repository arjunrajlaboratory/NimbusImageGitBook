# Citations

NimbusImage depends on countless contributions from scientists and engineers around the world. If you use NimbusImage, we recommend you cite the relevant papers to recognize these efforts. We also hope to publish a paper soon that you can cite for the use of NimbusImage itself.

## How to acknowledge NimbusImage and related software

We recommend including text along the following lines in your papers:

> We analyzed our image datasets using the NimbusImage platform, which is available here:\
> [https://github.com/arjunrajlaboratory/NimbusImage/](https://github.com/arjunrajlaboratory/NimbusImage/)\
> and hosted here:
>
> [https://www.nimbusimage.com/](https://www.nimbusimage.com/)
>
> We used the Cellpose and Cellpose retrain tools (1-3) to detect cells and the Piscis and Piscis retrain tools (4) to detect mRNA spots. We connected each mRNA spot to the nearest cell using the "Connect to nearest tool" as described in the NimbusImage documentation.

## Citations

### Cellpose

Cellpose works like magic for cell segmentation and is the product of extensive research and development by Carsen Stringer. They have a series of three papers on the topic, and we generally recommending citing all three. The first one describes the Cellpose algorithm, the second introduces retraining, and the third introduces image restoration and new, highly accurate models. The fourth paper is a preprint for Cellpose-SAM, which combines Cellpose with the Segment Anything Model (SAM) to enable versatile cell segmentation.

Here is the GitHub repository:\
[https://github.com/MouseLand/cellpose](https://github.com/MouseLand/cellpose)

Here are the papers:\
\
1\. Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (2021). [Cellpose: a generalist algorithm for cellular segmentation.](https://www.nature.com/articles/s41592-020-01018-x) _Nature methods, 18_(1), 100-106.\
\
Pachitariu, M. & Stringer, C. (2022). [Cellpose 2.0: how to train your own model.](https://www.nature.com/articles/s41592-022-01663-4) _Nature methods_, 1-8.\
\
Stringer, C. & Pachitariu, M. (2025). [Cellpose3: one-click image restoration for improved segmentation.](https://www.nature.com/articles/s41592-025-02595-5) _Nature Methods_.\
\
Pachitariu, M., Rariden, M., & Stringer, C. (2025). [Cellpose-SAM: superhuman generalization for cellular segmentation.](https://doi.org/10.1101/2025.04.28.651001) _bioRxiv_ 2025.04.28.651001.

### StarDist

StarDist is a powerful tool for cell and nuclei detection that uses star-convex polygons to accurately segment objects in microscopy images. It is particularly effective for nuclear segmentation and can work in both 2D and 3D.

Here is the GitHub repository:  
[https://github.com/stardist/stardist](https://github.com/stardist/stardist)

Here are the papers:  

1\. Schmidt, U., Weigert, M., Broaddus, C., & Myers, G. (2018). [Cell Detection with Star-Convex Polygons.](https://doi.org/10.1007/978-3-030-00934-2_30) _Medical Image Computing and Computer Assisted Intervention (MICCAI)_, 265-273.  

2\. Weigert, M., Schmidt, U., Haase, R., Sugawara, K., & Myers, G. (2020). [Star-convex Polyhedra for 3D Object Detection and Segmentation in Microscopy.](https://doi.org/10.1109/WACV45572.2020.9093435) _The IEEE Winter Conference on Applications of Computer Vision (WACV)_.  

3\. Weigert, M., & Schmidt, U. (2022). [Nuclei Instance Segmentation and Classification in Histopathology Images with Stardist.](https://doi.org/10.1109/ISBIC56247.2022.9854534) _The IEEE International Symposium on Biomedical Imaging Challenges (ISBIC)_.

### Segment Anything Model (SAM)

The Segment Anything Model (SAM) is a revolutionary promptable segmentation tool developed by Meta Research that can segment almost any object in an image based on simple prompts like points or boxes. NimbusImage incorporates SAM to enable rapid semi-automated segmentation with minimal user input.

Here is the GitHub repository:  
[https://github.com/facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything)

Here is the paper:  

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A.C., Lo, W.Y., Dollár, P., & Girshick, R. (2023). [Segment Anything.](https://arxiv.org/abs/2304.02643) _arXiv:2304.02643_.

### Piscis

Piscis is a specialized deep learning algorithm developed by Will Niu while in the Raj Lab. It is designed specifically for detecting diffraction-limited spots in fluorescence microscopy images, such as single RNA molecules in FISH experiments. It uses a novel loss function, the SmoothF1 loss, that directly penalizes false positives and false negatives while remaining differentiable for deep learning training.

Here is the GitHub repository:  
[https://github.com/zjniu/Piscis](https://github.com/zjniu/Piscis)

Here is the paper:  

Niu, Z., O'Farrell, A., Li, J., Reffsin, S., Jain, N., Dardani, I., Goyal, Y., & Raj, A. (2025). [Piscis: a novel loss estimator of the F1 score enables accurate spot detection in fluorescence microscopy images via deep learning.](https://doi.org/10.1101/2024.01.31.578123) _bioRxiv_, 2024.01.31.578123.


### CondensateNet

CondensateNet is a deep learning model developed by the Raj Lab for segmenting biomolecular condensates in brightfield microscopy images. It uses a Feature Pyramid Network (FPN) architecture with an EfficientNet encoder to detect and segment condensates.

Here is the GitHub repository:
[https://github.com/arjunrajlaboratory/condensatenet](https://github.com/arjunrajlaboratory/condensatenet)

Raj Lab. (2024). CondensateNet: Deep Learning for Biomolecular Condensate Segmentation. GitHub. [https://github.com/arjunrajlaboratory/condensatenet](https://github.com/arjunrajlaboratory/condensatenet)

## Packages

### Girder

Girder is a free and open source web-based data management platform developed by Kitware. It provides a flexible framework for storing, managing, and sharing various types of data, including large scientific and medical images.

Here is the GitHub repository:  
[https://github.com/girder/girder](https://github.com/girder/girder)

### Large Image

Large Image is a collection of Python modules developed and maintained by the Data & Analytics group at Kitware for processing large geospatial and medical images. It provides capabilities for tile serving, support for a wide variety of image formats, and efficient methods for accessing regions of large images.

Here is the GitHub repository:  
[https://github.com/girder/large_image](https://github.com/girder/large_image)

### GeoJS

GeoJS is a JavaScript library for visualizing geospatial data in a browser, developed by Kitware and OpenGeoscience. It aims to bridge the gap between GIS, scientific visualization, and information visualization, providing high-performance visualization and interactive data exploration of scientific and geospatial location-aware datasets.

Here is the GitHub repository:  
[https://github.com/OpenGeoscience/geojs](https://github.com/OpenGeoscience/geojs)

### DeepTile

DeepTile is a large image tiling and stitching library developed by the Arjun Raj Laboratory. It provides a standardized workflow for splitting large images into tiles of a specified size, processing tiles using regular Python functions, and stitching the processed tiles. DeepTile is especially useful for scaling Python functions and deep learning algorithms to arbitrarily large input image sizes.

Here is the GitHub repository:  
[https://github.com/arjunrajlaboratory/DeepTile](https://github.com/arjunrajlaboratory/DeepTile)


