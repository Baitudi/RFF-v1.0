
import json
import os

SCORE_LOG = "models/meta/phantom_score_log.json"
FEEDBACK_LOG = "models/meta/engine_feedback.txt"

def evaluate_meta_feedback():
    if not os.path.exists(SCORE_LOG):
        print("[Meta] No score log found.")
        return

    with open(SCORE_LOG, "r") as f:
        forks = json.load(f)

    if not forks:
        print("[Meta] No forks to analyze.")
        return

    total = len(forks)
    avg_score = round(sum([f["score"] for f in forks]) / total, 3)
    high_count = len([f for f in forks if f["score"] > 0.75])
    low_count = len([f for f in forks if f["score"] < 0.25])
    drift_rate = round(low_count / total, 3)

    report = f"""
    === META FEEDBACK REPORT ===
    Total Forks Tracked: {total}
    Average Score: {avg_score}
    High Confidence Forks: {high_count}
    Low Confidence Forks: {low_count}
    Drift Rate: {drift_rate}
    Recommendation: {"ADAPTIVE RECALIBRATION NEEDED" if drift_rate > 0.4 else "STABLE"}
    """

    with open(FEEDBACK_LOG, "w") as f:
        f.write(report.strip())

    print("[Meta] Feedback Report Generated.")
