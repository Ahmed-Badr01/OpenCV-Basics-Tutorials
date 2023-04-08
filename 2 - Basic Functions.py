import cv2
import numpy as np

img_path = 'Paste the path to your image file here'

img = cv2.imread('')

# To turn this color image into B/W, we can use:

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Takes the source, followed by the color code.

# To blur the image, we can use the Gaussian filter:

img_blurred = cv2.GaussianBlur(img, (5, 5), 3)  # Takes the source, followed by the kernel size, then sigma-x.
# Alternatively to specifying a number, we can also use "cv2.BORDER_DEFAULT".

# One way to detect edges is using the Canny edge detection function:

img_canny = cv2.Canny(img, 100, 100)  # Takes the source, then 2 thresholds (??). Higher thresholds = fewer edges.
# If we want to reduce the amount of detected edges, we can blur the image before using Canny on it.


# We sometimes need to make the detected edges in an image thicker, and we can do that using the dilate function.
# This will require an established kernel, which is a matrix of ones in this case, which we get to decide the size of.

kernel = np.ones((3, 3), dtype=np.uint8)

img_dilated = cv2.dilate(img_canny, kernel, iterations=1)  # We used img_canny here, cuz we're dealing with edges.

# We sometimes need to make the detected edges in an image thinner, and we can do that using the erode function.
# This will require an established kernel, like the dilation function.

img_eroded = cv2.erode(img_dilated, kernel, iterations=1)  # img_dilated or img_canny, cuz dealing with edges.

cv2.imshow('img_eroded', img_eroded)
cv2.waitKey(0)
