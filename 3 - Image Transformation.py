import numpy as np
import cv2

# In OpenCV, the origin (0,0) is in the top left corner of the screen.

# To resize an image, we'd like to first know its current size.

img = cv2.imread('Resources/bird.png')
print(img.shape)  # Prints: HEIGHT THEN WIDTH, then Number of Channels.

# To resize the image, we can use:

img_resized = cv2.resize(img, (295, 222))  # Takes the source, followed by the tuple of (WIDTH, HEIGHT).
cv2.imshow('resized bird', img_resized)
# cv2.waitKey(0)
print(img_resized.shape)

# A quick function to rescale a given frame to a given scale:


def rescale_frame(frame, scale=0.5):
    # Will work for images, video frames and webcam frames.
    new_width = frame.shape[1] * scale
    new_height = frame.shape[0] * scale
    dimensions = (new_width, new_height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)  # Dafuq does interpolation mean?


"""
From the OpenCV Documentation:

To shrink an image, it will generally look best with #INTER_AREA interpolation, whereas to
enlarge an image, it will generally look best with c#INTER_CUBIC (slow) or #INTER_LINEAR
(faster but still looks OK).
"""

# To change the properties of cam videos, one can also define a quick function:


def modify_cam_feed(cam, scale=0.75):
    # This function will only work with live cam feed.
    cam.set(3, 720)  # Set width to 720.
    cam.set(4, 480)  # Set Height to 480.
    cam.set(10, 100)  # Set the brightness to 100.


# To crop an image, we think of it as a matrix of pixels, and decide which sub-matrix we would like to keep.

img_cropped1 = img[0:443, 0:590]  # HEIGHT is the 1st argument, WIDTH is the 2nd.
cv2.imshow('crop1', img_cropped1)
cv2.waitKey(0)

# Translation: We can use cv2.warpAffine for that.


def translate(image, x_shift, y_shift):
    # x shift +ve -> right. x shift -ve -> left.
    # y shift +ve -> down. y shift -ve -> up.
    trans_matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    dimensions = (image.shape[1], image.shape[0])  # Remember: First is Height then Width in the shape!
    return cv2.warpAffine(image, trans_matrix, dimensions)


# Rotation: We can also use cv2.warpAffine for that.


def rotate(image, angle, rotation_center=None):
    height, width = image.shape[:2]

    if rotation_center is None:
        rotation_center = (width//2, height//2)

    rot_matrix = cv2.getRotationMatrix2D(rotation_center, angle, 1)  # Takes the rot_center, then angle, then scale.
    dimensions = (width, height)  # Remember: First is Height then Width in the shape!
    return cv2.warpAffine(image, rot_matrix, dimensions)


translated_img = translate(img, -100, -100)
cv2.imshow("Translated image", translated_img)
rotated_img = rotate(img, 60)
cv2.imshow("Rotated image", rotated_img)
rotated_twice_img = rotate(rotated_img, -100, (100, 100))
cv2.imshow("Rotated Twice image", rotated_twice_img)  # Rotating an image twice adds black bars from the 1st rotation.
vid = cv2.VideoCapture(0)
modify_cam_feed(vid)
cv2.waitKey(0)

# To flip an image, we use cv2.flip():

img_flipped = cv2.flip(img, 1)  # 1: Horizontal flip. 0: Vertical flip. -1: Both of them combined.
cv2.imshow('crop1', img_flipped)
cv2.waitKey(0)
