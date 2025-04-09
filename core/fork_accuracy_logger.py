import json
import os

fork_logs = []

def log_fork_result(frame, start, end, is_correct):
    fork_logs.append({
        "frame": frame,
        "start": start,
        "end": end,
        "correct": is_correct
    })

def export_logs_to_json(filepath="models/meta/accuracy_log.txt"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(fork_logs, f, indent=2)
    print(f"[📊] Accuracy log saved to {filepath}")
