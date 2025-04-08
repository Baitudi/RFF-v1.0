import cv2
import numpy as np
import os
import signal
import sys
import time

# === RFF Modules ===
from visual.visual_trail import draw_trail
from visual.prediction_overlay import draw_prediction_forks
from core import graph_parser
from core import rff_decision

# === Config ===
SNAPSHOT_FOLDER = "rff_dreams"
WINDOW_NAME = "RFF Tactical Viewport"
os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)

trail_points = []
MAX_TRAIL_LENGTH = 60
frame_counter = 0
snapshot_timer = time.time()

# === Shutdown Handler ===
def exit_handler(sig, frame):
    print("\n[INFO] Shutdown signal received. Cleaning up...")
    cv2.destroyAllWindows()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

# === Main Loop ===
while True:
    # --- 1. Capture chart + base frame ---
    frame, chart_data = graph_parser.capture_chart_and_player()

    # --- 2. Detect Player Position ---
    player_position = graph_parser.detect_player(chart_data)

    if player_position:
        trail_points.append(player_position)
        if len(trail_points) > MAX_TRAIL_LENGTH:
            trail_points.pop(0)

    # --- 3. Generate AI Fork Predictions ---
    forks = rff_decision.generate_prediction_forks(
        current_position=player_position,
        trail=trail_points,
        chart_image=chart_data
    )

    # --- 4. Visual Overlays ---
    frame = draw_trail(frame, trail_points)
    frame = draw_prediction_forks(frame, forks)

    # --- 5. Show in Window ---
    cv2.imshow(WINDOW_NAME, frame)

    # --- 6. Auto-Save Snapshot Every 3 Sec ---
    if time.time() - snapshot_timer >= 3:
        snapshot_path = os.path.join(SNAPSHOT_FOLDER, f"frame_{frame_counter:03}.png")
        cv2.imwrite(snapshot_path, frame)
        print(f"[INFO] Snapshot saved: {snapshot_path}")
        frame_counter += 1
        snapshot_timer = time.time()

    # --- 7. Manual Exit ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        print("[INFO] User exit triggered.")
        break

cv2.destroyAllWindows()
