
import cv2
import numpy as np
import signal
import sys

# Handle Ctrl+C gracefully
signal.signal(signal.SIGINT, lambda sig, frame: cv2.destroyAllWindows() or sys.exit(0))

# Load the image
img_path = "element.png"
image = cv2.imread(img_path)

if image is None:
    print("Failed to load image. Check path.")
    sys.exit(1)

image = cv2.resize(image, (1366, 768))



# === OUTER WALL DETECTION RANGE ===
lower_bgr = np.array([180, 200, 220])
upper_bgr = np.array([210, 230, 255])

# Create mask
mask = cv2.inRange(image, lower_bgr, upper_bgr)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out vertical/expiration line
filtered = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if h < w and all(pt[0][0] < 1200 for pt in contour):  # horizontal only and not far-right
        filtered.append(contour)

# Draw contours
debug_img = image.copy()
cv2.drawContours(debug_img, filtered, -1, (0, 255, 0), 2)

# Show results
cv2.imshow("Mask", mask)
cv2.imshow("Detected Contours", debug_img)
print("[🧠 INFO] Press ESC to exit windows.")

while True:
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()
