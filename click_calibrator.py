import pyautogui
import time

def calibrate_click(label):
    print(f"🖱️ Place your mouse over the {label} button in the next 5 seconds...")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"📌 {label} Button Position: x={x}, y={y}")
    return x, y

if __name__ == "__main__":
    print("=== RFF Click Calibrator ===")
    call_x, call_y = calibrate_click("CALL")
    put_x, put_y = calibrate_click("PUT")

    print("\n--- Copy These Values to action_executor.py ---")
    print(f"CALL_BUTTON_X = {call_x}")
    print(f"CALL_BUTTON_Y = {call_y}")
    print(f"PUT_BUTTON_X = {put_x}")
    print(f"PUT_BUTTON_Y = {put_y}")
