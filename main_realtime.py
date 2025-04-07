from feedback.rff_logger import log_decision
from feedback.rff_memory import build_confidence_map
from feedback.dream_engine import run_dream_batch
from feedback.rff_evolver import evolve_from_dreams
from core.action_executor import execute_trade, can_trade_now
from eye_viewport.viewport_core import launch_viewport

import threading
import time

# --- Launch Tactical HUD (EYE Viewport) in background ---
threading.Thread(target=launch_viewport, daemon=True).start()

# --- Example AI simulation logic (replace with real RFF AI decision system) ---
def get_ai_decision():
    # Replace with actual Flywheel AI decision logic
    predicted_action = "UP"  # or "DOWN" or "WAIT"
    confidence_score = 92.4  # from AI engine
    trail_snapshot = [(1000, 650), (1010, 660), (1020, 670)]  # from graph_parser
    purchase_time_left = 10  # Replace with real timer reading
    return predicted_action, confidence_score, trail_snapshot, purchase_time_left

# --- Meta Feedback Integration ---
decision_counter = 0
LOG_THRESHOLD = 5  # Run feedback logic every 5 decisions

def on_ai_decision(predicted_action, confidence_score, trail_snapshot, purchase_time_left):
    global decision_counter
    decision_counter += 1

    # Step 1: Log the current decision
    log_decision(
        chart_id="Chart4",
        decision=predicted_action,
        confidence=confidence_score,
        trail_snapshot=trail_snapshot,
        outcome=None
    )

    # Step 2: Auto-execute trade if valid
    if can_trade_now(purchase_time_left):
        execute_trade(predicted_action)
    else:
        print("[RFF] Purchase window closed — no trade executed.")

    # Step 3: Trigger feedback loop periodically
    if decision_counter % LOG_THRESHOLD == 0:
        print("[RFF] Running Meta Feedback Cycle...")

        # Update confidence map
        build_confidence_map()

        # Simulate alternate futures (dreams)
        threading.Thread(target=run_dream_batch, kwargs={"limit": 3}).start()

        # Evolve confidence scores based on simulations
        threading.Thread(target=evolve_from_dreams).start()

# --- Main Execution Loop (Simulation) ---
if __name__ == "__main__":
    print("[RFF] Main realtime engine started.")
    for _ in range(10):  # Simulate 10 AI decision cycles
        action, confidence, trail, timer = get_ai_decision()
        on_ai_decision(action, confidence, trail, timer)
        time.sleep(1)  # Simulated delay between decisions
