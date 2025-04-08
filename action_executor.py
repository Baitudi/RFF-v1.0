# action_executor.py

import pyautogui
import time

# Approximate screen coordinates for buttons (customize as needed)
CALL_BUTTON_POS = (1230, 930)
PUT_BUTTON_POS = (1380, 930)

def execute_trade(action):
    """
    Executes a trading action by simulating a click.

    Args:
        action (str): "CALL", "PUT", or "WAIT"
    """
    if action == "CALL":
        pyautogui.click(CALL_BUTTON_POS)
        print("[RFF] Executed CALL action.")
    elif action == "PUT":
        pyautogui.click(PUT_BUTTON_POS)
        print("[RFF] Executed PUT action.")
    elif action == "WAIT":
        print("[RFF] WAIT decision — no trade executed.")
    else:
        print(f"[RFF] Unknown action: {action}")
