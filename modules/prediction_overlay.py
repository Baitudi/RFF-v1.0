import cv2
import numpy as np
from core.trail_detector import detect_trail_live
from prediction_overlay import draw_forecast_overlay

# Simulated frame loop (placeholder for real-time screen input)
def main():
    cap = cv2.VideoCapture(0)  # Replace with screen grab or video feed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Simulated player position (use real detection in production)
        player_x, player_y = 100, 200

        # Draw the fork forecast overlay
        frame = draw_forecast_overlay(frame, player_x, player_y, scale_x=4, scale_y=1.8, base_confidence=0.85)

        cv2.imshow("RFF HUD", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
