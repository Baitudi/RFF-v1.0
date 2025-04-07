
import cv2
import numpy as np
import mss

# Chart 4 region for capture
chart4_region = {
    "top": 556,
    "left": 990,
    "width": 930,
    "height": 474
}

def show_image_and_get_bgr(image):
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            bgr = image[y, x]
            print(f"Clicked at ({x}, {y}) → BGR: {bgr}")

    cv2.imshow("Chart 4 Screenshot", image)
    cv2.setMouseCallback("Chart 4 Screenshot", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def capture_chart4():
    with mss.mss() as sct:
        screenshot = sct.grab(chart4_region)
        img = np.array(screenshot)
        img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        cv2.imwrite("chart4_click_sample.png", img_bgr)
        print("Screenshot saved as 'chart4_click_sample.png'")
        show_image_and_get_bgr(img_bgr)

if __name__ == "__main__":
    capture_chart4()
