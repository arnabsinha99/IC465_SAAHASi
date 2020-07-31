# Leaf Image Segmentation

### Objective

- Implement a technique that can segment(extract) leaf from an image containing leaf

### Resources

- Inspired by the paper: [Automatic Leaf Extraction from Outdoor
Images ](https://arxiv.org/pdf/1709.06437.pdf)

### Usage

- `python3 segment.py`

 __Command structure__
```
usage: segment [-h] [-m MARKER_INTENSITY] [-f {no,flood,threshold,morph}] [-s]
               [-d DESTINATION]
               image_source

positional arguments:
  image_source          A path of image filename or folder containing images

optional arguments:
  -h, --help            show this help message and exit
  -m MARKER_INTENSITY, --marker_intensity MARKER_INTENSITY
                        Output image will be as black background and
                        foreground with integer value specified here
  -f {no,flood,threshold,morph}, --fill {no,flood,threshold,morph}
                        Change hole filling technique for holes appearing in
                        segmented output
  -s, --smooth          Output image with smooth edges
  -d DESTINATION, --destination DESTINATION
                        Destination directory for output image. If not
                        specified destination directory will be input image
                        directory

```

### Examples:

__Command used__: `python3 segment.py 'some file or folder'`

__Input Images__
        
![alt Healthy Apple Leaf](testing_files/apple_healthy.JPG) ![alt Apple Leaf with Black Rot](testing_files/apple_black_rot.JPG)

__Output Images__

![alt Segmented Healthy Apple Leaf](testing_files/apple_healthy_marked.JPG) ![alt Segmented Apple Leaf with Black Rot](testing_files/apple_black_rot_marked.JPG)
