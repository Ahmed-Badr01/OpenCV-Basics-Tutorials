import cv2
import numpy as np

# First, we load the image within which we would like to change the perspective of an object.

cards = cv2.imread('Resources/card.png')
cv2.imshow('cards', cards)
cv2.waitKey(0)

# Then, we get the coordinates of the corners of the object (Here:cards). For now, we use paint to do that.
# Corners' coordinates: (312, 309), (386,212), (657,363), (677, 253).
# These are in the order: 1 2 : 3 4.

# We define the width and height of the new image that will form from warping the perspective of the object:
width, height = 250, 350  # These numbers maintain the original ratio of a playing card.

# We now define two np arrays containing the current borders of the object, and the final warped corners' coordinates.

original_object_borders = np.float32([[312, 309], [378, 216], [657, 363], [681, 257]])  # Type must be float32! (why?)
final_object_points = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype=np.float32)

# We now use OpenCV to calculate a matrix of numbers needed to perform the warping:
matrix = cv2.getPerspectiveTransform(original_object_borders, final_object_points)

# Finally, we perform the warping:
flat_card = cv2.warpPerspective(cards, matrix, (width, height))
# This takes the source, the matrix and the final (?) dimensions.

cv2.imshow('cards', cards)
cv2.imshow('flat card', flat_card)
cv2.waitKey(0)
