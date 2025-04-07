import cv2
import numpy as np

# Load images
foreground_img = cv2.imread("vision/element.png")
background_img = cv2.imread("vision/background.png")

if foreground_img is None or background_img is None:
    print("Image not found. Check filenames or paths.")
    exit()

# Resize background to match foreground size
background_img = cv2.resize(background_img, (foreground_img.shape[1], foreground_img.shape[0]))

# Subtract background (absolute difference)
diff = cv2.absdiff(foreground_img, background_img)

# Convert to grayscale and threshold to create mask
gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

# Apply mask to extract foreground
foreground_only = cv2.bitwise_and(foreground_img, foreground_img, mask=mask)

# Define BGR range for potential trail/player detection (green glow)
lower_bgr = np.array([0, 145, 40], dtype=np.uint8)
upper_bgr = np.array([0, 185, 55], dtype=np.uint8)
highlight_mask = cv2.inRange(foreground_only, lower_bgr, upper_bgr)
highlighted = cv2.bitwise_and(foreground_only, foreground_only, mask=highlight_mask)

# Display results
cv2.imshow("Original Chart (element.png)", foreground_img)
cv2.imshow("Background Cleaned", foreground_only)
cv2.imshow("Trail Highlight", highlighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
