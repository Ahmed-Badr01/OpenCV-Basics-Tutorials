import cv2
import numpy as np

img_bw_black = np.zeros((512, 512))  # Black and White image (2D) filled with Black.
img_black_colorable = np.zeros((512, 512, 3), dtype=np.uint8)
# data type is float64 by default. We make it uint8 to get values between 0 and 255, which are suitable for colors.

# To make a copy of the image we have, we can use the Numpy copy function:
img_color_blue = img_black_colorable.copy()
# Don't use new_img = old_img, as any changes to new_img will also change old_img.

# Now we can fill the color-able image with any specific color we want:
img_color_blue[:] = (255, 0, 0)  # Blue. Remember: (b, g, r) for OpenCV.

# We can also use this concept to color a specific rectangular region within the image.
img_color_blue[100: 400, 330:570] = (111, 111, 111)

cv2.imshow('img', img_black_colorable)
cv2.imshow('img2', img_color_blue)
cv2.waitKey(0)
print(img_black_colorable.dtype)
print(img_color_blue.shape)  # Shape didn't change, although the region specified for coloring went beyond the border.

"""
Side idea: quick loop that generates every possible mix of blue and red.
Took some ~250 Mbs and around 12 minutes to generate with Numpy on cpu.
Generated 65k images.

for i in range(256):
    for j in range(256):
        img = np.zeros((720, 720, 3), dtype=np.uint8)
        img[:] = (i, 0, j)
        cv2.imwrite(f"Resources/{i*256 + j}.png", img)
"""

# To draw a line, we can use:

cv2.line(img_color_blue, (0, 0), (512, 512), (0, 255, 0), 2)
# Takes the source image, then starting point of the line, then ending point, then color, then thickness (optional).

cv2.imshow('with line', img_color_blue)
cv2.waitKey(0)

# To draw a rectangle, we can use:

cv2.rectangle(img_color_blue, (0, 0), (300, 250), (0, 0, 255), 3)
# Takes the source image, then starting point of the rectangle, then ending point, color then thickness (optional).

# To draw a rectangle proportional to the image's dimensions, we can use something like:

cv2.rectangle(img_color_blue, (0, 0), (img_color_blue.shape[1]//2, img_color_blue.shape[0]//2), (0, 0, 255), 3)
# This creates a rectangle that fills the top-left corner of the screen. The floor division rounds numbers.

cv2.imshow('with rectangle', img_color_blue)
cv2.waitKey(0)

# To fill the rectangle, we replace the final argument (thickness) with cv2.FILLED:

cv2.rectangle(img_color_blue, (0, 0), (300, 250), (0, 0, 255), cv2.FILLED)
# We can also use '-1' for the thickness to fill the rectangle, or any shape.

cv2.imshow('with filled rectangle', img_color_blue)
cv2.waitKey(0)

# To draw a circle, we can use:

cv2.circle(img_color_blue, (250, 250), 50, (255, 0, 255), 3)
# Takes the source image, then center point of the circle, then radius, then color, then the thickness (optional).

# To draw a circle at the center of the image, for example, we can use:

cv2.circle(img_color_blue, (img_color_blue.shape[1]//2, img_color_blue.shape[0]//2), 50, (255, 0, 255), 3)

cv2.imshow('with circle', img_color_blue)
cv2.waitKey(0)

# To add text, we can use:

cv2.putText(img_color_blue, "OpenCV", (100, 100), cv2.FONT_ITALIC, 1.5, (255, 150, 255), 3)
# Takes the source image, then the text, then origin point, then font, then font size, color then thickness (optional).

cv2.imshow('with text', img_color_blue)
cv2.waitKey(0)
