import cv2
import matplotlib.pyplot as plt

image_path = 'element.png'
image = cv2.imread(image_path)

if image is None:
    print("Failed to load image. Check path.")
    exit()

clicked_colors = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = image[y, x]
        print(f"Clicked at ({x}, {y}) → BGR = [{b}, {g}, {r}]")
        clicked_colors.append((x, y, [b, g, r]))
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

cv2.namedWindow('Click to detect BGR - Press ESC to exit')
cv2.setMouseCallback('Click to detect BGR - Press ESC to exit', click_event)

while True:
    cv2.imshow('Click to detect BGR - Press ESC to exit', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()
