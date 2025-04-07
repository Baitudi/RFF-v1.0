import time
import threading
from core.trail_detector import detect_trail_live
from core.player_detector import detect_player_position
from core.timer_ocr import read_purchase_timer
from core.action_decider import decide_action
from feedback.rff_memory import build_confidence_map
from feedback.rff_evolver import evolve_from_dreams
from eye_viewport.viewport_core import launch_viewport
from eye_viewport.hud_data_feed import update_ai_insight
from action_executor import execute_trade

print("[RFF] Starting EYE Viewport...")

# Launch the HUD viewport in a separate thread
viewport_thread = threading.Thread(target=launch_viewport)
viewport_thread.start()

print("[RFF] Main realtime engine started.")

# --- Main Loop ---
try:
    while True:
        # 1. Read Timer
        timer = read_purchase_timer()

        # 2. Detect Player
        player_position = detect_player_position()

        # 3. Detect Trail
        trail = detect_trail_live()

        # 4. Decision Engine
        action, confidence = decide_action(trail, player_position, timer)

        # 5. Execute Trade
        if action in ['CALL', 'PUT']:
            execute_trade(action)
            print(f"[RFF] Executed {action} action.")
        else:
            print("[RFF] WAIT decision — no trade executed.")

        # 6. Update AI HUD Insight
        update_ai_insight(confidence)

        # 7. Meta Feedback + Dream Loop
        if int(time.time()) % 10 == 0:
            print("[RFF] Running Meta Feedback Cycle...")
            build_confidence_map()
            threading.Thread(target=evolve_from_dreams).start()

        # 8. Small delay
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[RFF] Terminated by user.")
