---
description: Files you can import to NimbusImage.
---

# File formats

NimbusImage can read most file formats "out of the box", so mostly you will not have to worry about it. Here, we describe a few considerations for some common formats here. Also, **please do let us know if you are having trouble importing your data.** We have tried to make it as easy and compatible as possible, but there are a quasi-infinite number of formats, so we are sure there are many cases we have not yet encountered.

## Nikon (.nd2)

Nikon .nd2 files work essentially out of the box. You can just import them, and the variable assignment should work, and you generally will not need to enable "Transcode to optimized TIFF". If you have a large tiled image, it would be best to stitch the image in Nikon Elements first, if possible. If, however, that is not an option because the file is too large, you can enable "Composite stage positions" and "Transcode to optimized TIFF" and that should be able to do the stitching for you (although that has not been as extensively tested on our end).

## Zeiss (.czi)

Zeiss .czi files work out of the box as well. The only difference is that we have found that performance is better when these files are transcoded inot a TIFF, so by default "Transcode to optimized TIFF" is enabled.

## Leica (.lif)

Leica .lif files are somewhat more complex, because they are more like containers that can contain multiple image sets. For instance, a .lif file could contain a time lapse, a set of Z-stacks, and a few individual multi-channel images. NimbusImage does not currently import multiple datasets at once. Hence, **for .lif files, we select the largest image set and import that one.** We recommend breaking up your .lif file accordingly so that the outcome is predictable. If enough users ask for the feature, we may enable the ability to choose amongst the image sets or allow for multiple imports.

## TIFF and OME-TIFF

Ah yes, TIFF… So TIFF can be imported, and if the variables are set within the TIFF, they will be read.

{% hint style="info" %}
By default, "Transcode into optimized TIFF" is enabled because, in our experience, most TIFF files are not well optimized. Certainly, if you have multiple TIFF files, we would strongly recommend transcoding them. Only disable this option if you know for sure that the TIFF is optimized (for an example, see below).
{% endhint %}

Most TIFFs work fine, but there is an issue with OME-TIFFs that are spread across multiple files. An OME-TIFF can sometimes have a single file that points to multiple files in a series. This sort of file is not yet supported out of the box, in that you cannot upload all the files and import them directly. However, you can convert this into a single tiff file pretty easily and then import it. Do the following:

```
pip install large_image # installs the large_image package
large_image_converter first_file_in_series.ome.tiff outputfile.tiff
```

This will generate `outputfile.tiff` that then can be directly imported into NimbusImage. **In this case, you do NOT need to transcode into an optimized TIFF**, because `large_image_converter` has already done that for you.

## TIFFs from IncuCyte

The IncuCyte outputs files in a VERY annoying way. They can be directly read into NimbusImage, and it will do its best to handle the naming conventions, but it can be irritating because if you have multi-channel images, it exports them all with the _exact same file names_. Ugh. Anyway, we wrote a little script you can use to clean up the IncuCyte TIFFs and rename them:

[https://github.com/arjunrajlaboratory/process\_incucyte\_tiff\_data](https://github.com/arjunrajlaboratory/process_incucyte_tiff_data)

{% hint style="info" %}
Follow the directory structure very carefully. Also, if you just have a single channel, you still have to have a "phase" subdirectory in which all your files will live.
{% endhint %}
