import cv2
import numpy as np

# Load your screenshot manually
img = cv2.imread('your_screenshot.png')  # Put screenshot in the same folder as this script

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color_bgr = img[y, x]
        print(f"Clicked at ({x},{y}) - BGR Color: {color_bgr}")

cv2.imshow('Click Anywhere on Playing Area', img)
cv2.setMouseCallback('Click Anywhere on Playing Area', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
