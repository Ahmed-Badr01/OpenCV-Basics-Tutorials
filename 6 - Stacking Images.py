"""This script looks different from the one Murtaza made in his video, but most if not all of the changes are renames and reformats of the same codes."""

import cv2
import copy
import numpy as np


def stack_images(image_list, columns, scale):
    """ Stack Images together to display in a single window.
    parameters:
    image_list: list of images to stack
    columns: the number of images in a row
    scale: bigger than 1 -> enlarge and smaller than 1 -> shrink.
    returns: Stacked Image """
    img_list = copy.deepcopy(image_list)

    # Make the array full by adding blank image(s) to fill the row, otherwise OpenCV can't work:
    total_images = len(img_list)

    if total_images % columns == 0:  # Check if total images can fit a matrix with the given no. of columns perfectly.
        rows = total_images // columns
    else:
        rows = (total_images // columns) + 1

    blank_images_count = (columns * rows) - total_images

    width = img_list[0].shape[1]
    height = img_list[0].shape[0]
    blank_img = np.zeros((height, width, 3), dtype=np.uint8)
    img_list.extend([blank_img] * blank_images_count)

    # Rescale the images and turn b/w images into bgr, so the number of channels is equal for all images,
    # and they can be stacked with Numpy:
    for i in range(columns * rows):
        img_list[i] = cv2.resize(img_list[i], (0, 0), None, scale, scale)

        if len(img_list[i].shape) == 2:
            img_list[i] = cv2.cvtColor(img_list[i], cv2.COLOR_GRAY2BGR)

    # Put the images in a matrix:

    stacked_rows = [blank_img] * rows

    for i in range(rows):
        row = []  # Initialize an empty row.

        for j in range(columns):
            row.append(img_list[i * columns + j])  # Append all images from the row in the images list.

        stacked_rows[i] = np.hstack(row)  # Horizontally stack the row together into one element, and save it.

    matrix = np.vstack(stacked_rows)  # Vertically stack the rows together into one element representing the matrix.

    return matrix
