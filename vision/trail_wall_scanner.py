import cv2
import numpy as np
import mss

# Region of Chart 4 (Bottom-Right)
chart4_region = {
    "top": 556,
    "left": 990,
    "width": 930,
    "height": 474
}

# Calibrated BGR target colors with tolerance buffer
targets = {
    "trail": ([83, 111, 130], [103, 131, 150]),
    "inner_wall": ([198, 158, 100], [218, 178, 120]),
    "outer_wall": ([66, 70, 188], [86, 90, 208]),
    "playing_area": ([192, 138, 41], [212, 158, 61])
}

def segment_chart4():
    with mss.mss() as sct:
        screenshot = sct.grab(chart4_region)
        img = np.array(screenshot)
        img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        for label, (lower, upper) in targets.items():
            lower_np = np.array(lower, dtype=np.uint8)
            upper_np = np.array(upper, dtype=np.uint8)

            mask = cv2.inRange(img_bgr, lower_np, upper_np)
            result = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            debug_img = img_bgr.copy()
            cv2.drawContours(debug_img, contours, -1, (0, 255, 255), 1)

            cv2.imwrite(f"{label}_mask.png", result)
            cv2.imwrite(f"{label}_contours.png", debug_img)

            print(f"{label.capitalize()} processed. Contours found: {len(contours)}")

if __name__ == "__main__":
    segment_chart4()
