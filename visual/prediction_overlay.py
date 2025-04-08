import cv2

def draw_prediction_forks(frame, forks):
    """
    Draws directional AI forks with confidence glow on the frame.

    Parameters:
    - frame: The image/frame to draw on
    - forks: A list of dicts with keys:
        - 'start': (x1, y1) - starting point of arrow
        - 'end': (x2, y2) - ending point of arrow
        - 'confidence': float from 0.0 to 1.0
    """
    for fork in forks:
        start = fork['start']
        end = fork['end']
        confidence = fork.get('confidence', 0.5)

        # Color based on confidence level
        if confidence >= 0.75:
            color = (0, 255, 0)      # Green
        elif confidence >= 0.4:
            color = (0, 165, 255)    # Orange
        else:
            color = (0, 0, 255)      # Red

        thickness = int(2 + confidence * 4)
        cv2.arrowedLine(frame, start, end, color, thickness, tipLength=0.3)

    return frame
