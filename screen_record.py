# rff_custom_recorder.py

import cv2
import numpy as np
import mss
import time

def record_custom_area(
    filename="rff_trade_flow.avi",
    duration_sec=90,  # 1.5 minutes
    fps=20,
    top=600,
    left=1000,
    width=800,
    height=400
):
    monitor = {
        "top": top,
        "left": left,
        "width": width,
        "height": height
    }

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    with mss.mss() as sct:
        print(f"[REC] Recording {width}x{height} at ({left},{top}) for {duration_sec}s...")

        start_time = time.time()
        while True:
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            out.write(frame)
            cv2.imshow("RFF Trade Session Recording", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[REC] Manually stopped.")
                break

            if (time.time() - start_time) > duration_sec:
                print("[REC] Finished 1.5 min recording.")
                break

        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 👉 Set your custom size here based on what you want to show
    record_custom_area(
        filename="chart4_trading_replay.avi",
        duration_sec=90,  # 1.5 minutes
        fps=20,
        top=360,          # Adjust as per your screen
        left=60,
        width=600,        # Wider if you want to capture buttons/timer
        height=350
    )
