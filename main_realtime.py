import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
from visual.replay_exporter import export_replay
import time
import os
import cv2
from core.phantom_engine import PhantomEngine
from core.phantom_model_loader import load_phantom_model
from visual.ghost_learning_hud import draw_ghost_overlay
from visual.prediction_fork_overlay import render_prediction_overlay
from core.fork_accuracy_logger import log_fork_result, export_logs_to_json
from visual.replayer_scoring_overlay import draw_accuracy_score
from visual.trail_fork_validator import find_trail_points, is_fork_valid
from visual.trail_rewind import rewind_trail

# Assuming trail_points = list of (x, y)

# Optional log path
accuracy_log = "feedback/accuracy_log.txt"
os.makedirs("feedback", exist_ok=True)

# Init Phantom Engine
phantom = PhantomEngine()
model = load_phantom_model()
if model:
    phantom.inject_failed_forks(model["drift_patterns"])

# Start main loop
frame_index = 0
    frames_to_export = []  # For video export
while True:
    # Simulated test chart (normally from live screen)
    img = 255 * np.ones((300, 500, 3), dtype=np.uint8)
    trail_points = find_trail_points(img)
    img = rewind_trail(img, trail_points)
    current_position = (250, 150)  # Simulated player

    # Run phantom fork predictions
    forks = phantom.generate_phantom_forks(current_position, momentum=1.5)

    # Draw overlays
    ghosted = draw_ghost_overlay(img.copy(), forks)
    overlayed = render_prediction_overlay(ghosted, forks)

    # Show result
    cv2.putText(overlayed, f"Frame {frame_index}", (10, 290),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
    frames_to_export.append(img.copy())
    cv2.imshow("RFF LIVE HUD", overlayed)

    # Log prediction result (simulation)
    with open(accuracy_log, "a") as log:
        for f in forks:
            log.write(f"{frame_index},{f['point']},{f['confidence']}\n")

    key = cv2.waitKey(200)
    if key == ord('q') or key == 27:
        print("[EXIT] Closing HUD...")
        break

    frame_index += 1

cv2.destroyAllWindows()
    export_replay(frames_to_export)