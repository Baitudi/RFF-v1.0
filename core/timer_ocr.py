# OCR logic for reading the purchase timer
# core/timer_ocr.py

import pytesseract
import cv2
import numpy as np
from PIL import ImageGrab

# Define Chart 4 timer read zone
TIMER_REGION = (990, 556, 930, 474)  # (x, y, w, h)

def preprocess_image_for_ocr(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
    return binary

def read_purchase_timer():
    """
    Capture timer area and use OCR to read the time.
    Returns an integer of seconds left or None if not found.
    """
    x, y, w, h = TIMER_REGION
    screenshot = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
    image_bgr = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    processed = preprocess_image_for_ocr(image_bgr)
    
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(processed, config=custom_config)

    # Extract the first number found
    digits = ''.join(filter(str.isdigit, text))
    if digits:
        return int(digits)
    
    return None
