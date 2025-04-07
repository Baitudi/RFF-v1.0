# core/timer_ocr.py

import cv2
import pytesseract
import os
import numpy as np

# === CONFIG ===
MASKS_FOLDER = os.path.join(os.path.dirname(__file__), "..", "masks")
LAST_GOOD = {"seconds": -1, "phase": "UNKNOWN"}

# === 1. Icon Mask Filtering ===
def load_masks():
    masks = []
    for file in os.listdir(MASKS_FOLDER):
        path = os.path.join(MASKS_FOLDER, file)
        mask = cv2.imread(path)
        if mask is not None:
            masks.append(mask)
    return masks

def apply_icon_masks(frame, masks):
    masked = frame.copy()
    for mask in masks:
        res = cv2.matchTemplate(masked, mask, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        threshold = 0.8
        if max_val >= threshold:
            h, w = mask.shape[:2]
            cv2.rectangle(masked, max_loc, (max_loc[0]+w, max_loc[1]+h), (255,255,255), -1)
    return masked

# === 2. Phase Classification ===
def classify_phase(seconds, previous_seconds):
    if seconds == -1:
        return LAST_GOOD["phase"]
    if seconds >= 40:
        return "IDLE"
    elif 10 <= seconds < 40:
        return "EXPIRATION"
    elif 0 <= seconds < 10:
        if previous_seconds > seconds:
            return "PURCHASE"
        else:
            return "IDLE"
    return "UNKNOWN"

# === 3. OCR Reader with Filtering ===
def read_purchase_timer(full_img, previous_seconds=-1, debug_overlay=False):
    global LAST_GOOD

    # Crop extended region from Chart 4 (990, 556, 930, 474)
    timer_region = full_img[556:556+474, 990:990+930]

    # Load and apply masks
    masks = load_masks()
    masked_img = apply_icon_masks(timer_region, masks)

    # Preprocess
    gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # OCR config: digits only
    config = "--psm 7 -c tessedit_char_whitelist=0123456789"
    raw_text = pytesseract.image_to_string(thresh, config=config).strip()

    # Clean & extract digits
    digits_only = ''.join(filter(str.isdigit, raw_text))

    # Fallback if OCR is trash
    if len(digits_only) == 0:
        return LAST_GOOD["seconds"], LAST_GOOD["phase"]

    try:
        # Attempt to parse clean 2-digit time
        if len(digits_only) >= 2:
            seconds = int(digits_only[-2:])  # take last 2 digits only
        else:
            seconds = int(digits_only)
    except:
        return LAST_GOOD["seconds"], LAST_GOOD["phase"]

    # Phase classification
    phase = classify_phase(seconds, previous_seconds)

    # Update memory
    LAST_GOOD = {"seconds": seconds, "phase": phase}

    # Optional overlay
    if debug_overlay:
        cv2.putText(timer_region, f"OCR: {seconds}s | Phase: {phase}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.imshow("Timer OCR Debug", timer_region)

    return seconds, phase
