#!/usr/bin/env python3
import cv2
import numpy

image = cv2.imread('test.jpeg')
height, width, channels = image.shape

# Loop through each pixel by index
for y, x in numpy.ndindex(height, width):
    # Access the pixel at position (y, x)
    pixel = image[y, x]

    # For now let's just print some pixel information
    # We'll skip lots of pixels to keep runtimes manageable
    if y % 100 == 0 and x % 100 == 0:
        print(f"Pixel [{x}, {y}]: {pixel}")
