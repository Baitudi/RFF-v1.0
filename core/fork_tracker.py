
import json
import os

log_data = []

def log_fork_result(frame_index, start, end, success):
    log_data.append({
        "frame": frame_index,
        "start": start,
        "end": end,
        "success": success
    })

def export_logs_to_json(path="models/meta/accuracy_log.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(log_data, f, indent=2)
    print(f"[LOG] Accuracy data exported to: {path}")
