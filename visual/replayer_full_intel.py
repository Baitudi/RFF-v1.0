# replayer_full_intel.py – with Ghost Memory Overlay

import cv2
import os
import numpy as np
import math
from core import fork_tracker
from visual.fork_glow_renderer import draw_fork_with_glow
from visual.fork_zone_mapper import highlight_convergence_zones
from visual.ghost_learning_hud import draw_ghost_memory
from phantom_engine import PhantomEngine

TRAIL_COLOR = (0, 255, 0)
TRAIL_TOLERANCE = 20

phantom = PhantomEngine()

def find_trail_points(image):
    lower = np.array([max(0, c - TRAIL_TOLERANCE) for c in TRAIL_COLOR], dtype=np.uint8)
    upper = np.array([min(255, c + TRAIL_TOLERANCE) for c in TRAIL_COLOR], dtype=np.uint8)
    mask = cv2.inRange(image, lower, upper)
    points = cv2.findNonZero(mask)
    return [tuple(pt[0]) for pt in points] if points is not None else []

def average_direction(trail):
    if len(trail) < 2: return None
    p1, p2 = trail[-2], trail[-1]
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return math.degrees(math.atan2(dy, dx))

def angle_difference(a1, a2):
    return min(abs(a1 - a2), 360 - abs(a1 - a2))

def run_replayer_full_intel(folder_path="rff_dreams", delay=0.4):
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    image_files = sorted([f for f in os.listdir(folder_path) if f.endswith((".png", ".jpg"))])
    total_forks, correct_forks = 0, 0

    for idx, file in enumerate(image_files):
        frame = cv2.imread(os.path.join(folder_path, file))
        trail = find_trail_points(frame)
        angle_actual = average_direction(trail)
        if angle_actual is None: continue

        origin = trail[-1]
        forks = []
        for offset in [-30, -15, 0, 15, 30]:
            angle = angle_actual + offset
            rad = math.radians(angle)
            end = (int(origin[0] + math.cos(rad) * 80), int(origin[1] + math.sin(rad) * 80))
            forks.append({"start": origin, "end": end, "angle": angle})

        best = min(forks, key=lambda f: angle_difference(f["angle"], angle_actual))

        for fork in forks:
            diff = angle_difference(fork["angle"], angle_actual)
            confidence = max(0.1, 1 - (diff / 45))
            frame = draw_fork_with_glow(frame, fork["start"], fork["end"], confidence)

            is_success = (fork == best and diff < 20)
            if fork == best:
                if is_success: correct_forks += 1
                phantom.record_fork(origin, fork["end"], is_success)
                fork_tracker.log_fork_result(idx, fork["start"], fork["end"], is_success)
        total_forks += 1

        # 🔮 Draw ghost memory trail
        ghost_path = phantom.get_ghost_path(steps=5)
        frame = draw_ghost_memory(frame, ghost_path)

        # 💡 Draw convergence zones and accuracy score
        frame = highlight_convergence_zones(frame, forks)
        accuracy = int((correct_forks / total_forks) * 100)
        cv2.putText(frame, f"AI Accuracy: {accuracy}%", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        # 🖥️ Show frame
        cv2.imshow("RFF Replay: Phase 7 + Ghost HUD", frame)
        if cv2.waitKey(int(delay * 1000)) in [27, ord('q')]: break

    cv2.destroyAllWindows()
    fork_tracker.export_logs_to_json("models/meta/accuracy_log.txt")
