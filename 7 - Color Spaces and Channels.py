import matplotlib.pyplot as plt
import numpy as np
import cv2

# Color spaces are systems of representing colors. Some examples are RGB, BGR, HSV and GRAY.

image = cv2.imread(f"Resources/bird.png")
cv2.imshow('BGR image', image)
cv2.waitKey(0)

# BGR to GRAY:
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray)
cv2.waitKey(0)

# BGR to HSV:
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv)
cv2.waitKey(0)

# BGR to LAB:
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB image', lab)
cv2.waitKey(0)

# BGR to RGB (useful for precessing images that were read by OpenCV but need to be processed by other libraries):
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB image', rgb)
cv2.waitKey(0)
# The difference can be noticed when we compare the OpenCV interpretation of the RGB image with that of Matplotlib:
plt.imshow(rgb)
plt.show()

# Note: To convert from GRAY to HSV or LAB, we have to first convert to BGR and then to HSV, otherwise it doesn't work.
bgr_step = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
hsv = cv2.cvtColor(bgr_step, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv)
cv2.waitKey(0)

# ----------------------------------------------------------------------------- #

# Color channels are what makes up an image. We can split them if we want process them individually,
# and then merge them back if we want.

# We split an image into its individual channels using cv2.split():
b, g, r = cv2.split(image)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.waitKey(0)

# A single color channel is represented as a B/W image that shows the intensity of the color on that scale.
# One can also visualise a single channel by merging it with another 2 blank channels:
blank_channel = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
blue = cv2.merge([b, blank_channel, blank_channel])
green = cv2.merge([blank_channel, g, blank_channel])
red = cv2.merge([blank_channel, blank_channel, r])
cv2.imshow('Visible Blue', blue)
cv2.imshow('Visible Green', green)
cv2.imshow('Visible Red', red)
cv2.waitKey(0)
