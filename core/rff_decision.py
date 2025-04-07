# core/rff_decision.py

import time
import json
import os

# ✅ Safe local log folder for Mac
LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "rff_decision_logs")
os.makedirs(LOG_PATH, exist_ok=True)

def log_decision_cycle(data):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    entry = {
        "time": timestamp,
        "phase": data.get("phase"),
        "seconds_left": data.get("seconds_left"),
        "player_position": data.get("player_position"),
        "decision": data.get("decision"),
    }

    file_path = os.path.join(LOG_PATH, f"{timestamp}_log.json")
    with open(file_path, "w") as f:
        json.dump(entry, f, indent=2)

def make_decision(data):
    """
    Make decisions based on trading phase and player position.
    """
    seconds = data.get("seconds_left", -1)
    phase = data.get("phase", "UNKNOWN")
    player_pos = data.get("player_position", None)

    decision = "WAIT"

    if phase == "IDLE":
        if not player_pos:
            decision = "WAIT"
        else:
            x, _ = player_pos
            if x < 200:
                decision = "DOWN"
            elif x > 500:
                decision = "UP"
            else:
                decision = "WAIT"

    elif phase == "PURCHASE":
        decision = "LOCKED"

    elif phase == "EXPIRATION":
        decision = "WAIT"

    else:
        decision = "WAIT"

    # Store for analysis
    data["decision"] = decision
    log_decision_cycle(data)

    return decision
