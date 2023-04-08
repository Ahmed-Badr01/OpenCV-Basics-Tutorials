import cv2
import keyboard

# To read images, we use cv2.imread(r'path'):

img_path = r'Paste the path to your image file here' 
# r stands for raw. This stops Python from escaping characters like "\", meaning the path can pasted as-is.

img = cv2.imread(img_path)

# To show images, we use cv2.imshow('output_window_name', image_variable):
# We also use cv2.waitkey(no_of_millisecs) '0 = until closed' to keep the image showing for a specified amount of time.

cv2.imshow('Image window title', img)
cv2.waitKey(0)

# To read videos, we use cv2.VideoCapture('path'):

vid = cv2.VideoCapture(r'video path')

# To show the video, OpenCV turn it into images, and then shows the images in a while loop using cv2.imshow:
# If we try to skip the 'if cv2.waitkey(number)' part altogether, the video will fail to show.
# We can use 'keyboard.is_pressed('key')' instead of the weird '0xFF == ord('key')' part.

while True:
    success, frame = vid.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(27) & keyboard.is_pressed('q'):  # Adds a delay between frames and waits for 'q' to break.
        break

# To read webcam feed, we use the exact same process, with a few (optional) additions:
# Using .set() only works on Webcam feeds. Does not work on Images or Videos!

vid = cv2.VideoCapture(0)  # 0 is the ID of the main webcam, use subsequent numbers if more webcams are present.
vid.set(3, 720)  # Set width to 720.
vid.set(4, 480)  # Set Height to 480.
vid.set(10, 100)  # Set Brightness to 100 (?).

while True:
    success, frame = vid.read()
    cv2.imshow('Cam', frame)
    if cv2.waitKey(27) & keyboard.is_pressed('q'):  # Adds a delay between frames and waits for 'q' to break.
        break

# Alternative way to close all windows at the end of a video capture loop:
vid.release()  # Deallocates the dedicated amount of memory occupied by the variable.
cv2.destroyAllWindows()  # Destroys all open windows.
