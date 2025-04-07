import os
import json
from datetime import datetime

LOG_DIR = "rff_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_decision(chart_id, decision, confidence, trail_snapshot, outcome=None):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_entry = {
        "timestamp": timestamp,
        "chart": chart_id,
        "decision": decision,
        "confidence": confidence,
        "trail": trail_snapshot,
        "outcome": outcome
    }
    
    filename = os.path.join(LOG_DIR, f"{timestamp}_decision.json")
    with open(filename, "w") as f:
        json.dump(log_entry, f, indent=2)
