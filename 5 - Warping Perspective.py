"""This tutorial is hard to follow without watching the relevant section of the original video: https://youtu.be/WQeoO7MI0Bs?t=2700
You need to provide an image of an object which has similar properties as the one use din the video to be able to work your way through the example."""

import cv2
import numpy as np

# First, we load the image within which we would like to change the perspective of an object.

img_path = r'Paste the path to your image file here' 
# r stands for raw. This stops Python from escaping characters like "\", meaning the path can pasted as-is.

img = cv2.imread(img_path)

cards = cv2.imread(img_path)
cv2.imshow('cards', cards)
cv2.waitKey(0)

# Then, we get the coordinates of the corners of the object (Mine:cards). I used paint to do that.
# Corners' coordinates in my case: (x1, y1), (x2, y2), (x3, y3), (x4, y4).
# These are in the order: 1 2 : 3 4.

corners = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# We define the width and height of the new image that will form from warping the perspective of the object:
width, height = 250, 350  # These numbers maintain the original ratio of a playing card. Change if needed.

# We now define two np arrays containing the current borders of the object, and the final warped corners' coordinates.

original_object_borders = np.float32(corner for corner in corners)  # Type must be float32, according to the video
final_object_points = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype=np.float32)

# We now use OpenCV to calculate a matrix of numbers needed to perform the warping:
matrix = cv2.getPerspectiveTransform(original_object_borders, final_object_points)

# Finally, we perform the warping:
flat_card = cv2.warpPerspective(cards, matrix, (width, height))

cv2.imshow('cards', cards)
cv2.imshow('flat card', flat_card)
cv2.waitKey(0)
