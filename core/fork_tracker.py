fork_log = []

def log_fork_result(frame_index, fork_start, fork_end, is_correct):
    """
    Log a fork prediction result.

    Params:
        frame_index: current frame number
        fork_start: (x, y) start point
        fork_end: (x, y) end point
        is_correct: bool — did the fork match actual movement?
    """
    entry = {
        "frame": frame_index,
        "start": fork_start,
        "end": fork_end,
        "correct": is_correct
    }
    fork_log.append(entry)

def get_all_logs():
    """Returns the full list of fork results."""
    return fork_log

def get_accuracy():
    """Returns overall prediction accuracy as a %."""
    if not fork_log:
        return 0.0
    correct = sum(1 for entry in fork_log if entry["correct"])
    return round((correct / len(fork_log)) * 100, 2)

def export_logs_to_json(path="fork_log.json"):
    """Optional: Save results to a .json file for later use."""
    import json
    with open(path, "w") as f:
        json.dump(fork_log, f, indent=2)
