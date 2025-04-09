
import cv2
import numpy as np

def draw_score_heatmap(frame, score_data):
    overlay = np.zeros_like(frame)
    for entry in score_data:
        end = tuple(entry["end"])
        score = entry["score"]
        color = (0, int(255 * score), int(255 * (1 - score)))
        cv2.circle(overlay, end, 6, color, -1)
    return cv2.addWeighted(frame, 1.0, overlay, 0.4, 0)
