# eye_viewport/hud_data_feed.py

ai_insight_state = {
    "accuracy": 0.0,
    "learning_rate": 0.0,
    "active_forks": 0,
    "wait_decisions": 0,
    "memory_loops": 0
}

def update_ai_insight(accuracy=None, learning_rate=None, active_forks=None, wait_decisions=None, memory_loops=None):
    if accuracy is not None:
        ai_insight_state["accuracy"] = round(accuracy, 2)
    if learning_rate is not None:
        ai_insight_state["learning_rate"] = round(learning_rate, 3)
    if active_forks is not None:
        ai_insight_state["active_forks"] = active_forks
    if wait_decisions is not None:
        ai_insight_state["wait_decisions"] = wait_decisions
    if memory_loops is not None:
        ai_insight_state["memory_loops"] = memory_loops

def get_ai_insight():
    return ai_insight_state
