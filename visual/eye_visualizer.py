# visual/eye_visualizer.py

import cv2

# Colors (BGR)
PLAYER_COLOR = (0, 255, 0)         # Green circle
TEXT_COLOR = (0, 0, 0)             # Black
WAIT_COLOR = (51, 51, 51)          # #333333
UP_COLOR = (1, 155, 47)            # #019B2F
DOWN_COLOR = (215, 78, 58)         # #D74E3A
BG_COLOR = (255, 255, 255)         # White

def draw_player(img, position):
    if position:
        cv2.circle(img, position, 8, PLAYER_COLOR, -1)
        cv2.putText(img, "Player", (position[0] + 10, position[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_COLOR, 1)

def draw_decision(img, decision):
    h, w = img.shape[:2]
    color = TEXT_COLOR

    if decision == "UP":
        color = UP_COLOR
    elif decision == "DOWN":
        color = DOWN_COLOR
    elif decision == "WAIT":
        color = WAIT_COLOR

    cv2.putText(
        img,
        f"Decision: {decision}",
        (10, h - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

def draw_timer(img, seconds):
    cv2.putText(
        img,
        f"Time Left: {seconds if seconds >= 0 else 'N/A'}s",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 0),
        2
    )

def show_eye_view(chart_img, detection_data, decision):
    # Clone the image to avoid modifying original
    output = chart_img.copy()

    # Draw elements
    draw_player(output, detection_data.get("player_position"))
    draw_decision(output, decision)
    draw_timer(output, detection_data.get("seconds_left", -1))

    # Show final visual
    cv2.imshow("RFF EYE VIEW", output)
