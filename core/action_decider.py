# core/action_decider.py

import random

def decide_action(trail, player_position, timer):
    """
    Decide whether to CALL, PUT, or WAIT based on current trail, player, and timer.

    Parameters:
        trail (list): The historical trail points.
        player_position (tuple): The current (x, y) position of the player.
        timer (int or float): The seconds left before expiration.

    Returns:
        action (str): One of 'CALL', 'PUT', or 'WAIT'.
        confidence (float): A value between 0 and 1 indicating AI confidence.
    """
    
    # Default fallback
    action = "WAIT"
    confidence = 0.0

    # Extract basic directional info from trail
    if len(trail) >= 2:
        dx = trail[-1][0] - trail[-2][0]
        dy = trail[-1][1] - trail[-2][1]

        # Example simple rule: upward movement
        if dy < 0:
            action = "CALL"
            confidence = min(1.0, abs(dy) / 10)
        elif dy > 0:
            action = "PUT"
            confidence = min(1.0, abs(dy) / 10)
        else:
            action = "WAIT"
            confidence = 0.5

    # Modify decision based on timer
    if timer is not None and timer < 1:
        action = "WAIT"
        confidence = 0.0

    return action, confidence
