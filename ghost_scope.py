# ghost_scope.py - Final Ghost Overlay for Alignment

import cv2
import numpy as np

# Screen resolution (your Mac)
screen_width = 1920
screen_height = 1080

# Ghost Box (Purchase Zone area)
ghost_top = 140
ghost_left = 100
ghost_width = 1628
ghost_height = 845

overlay = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

# Draw the Ghost Box
cv2.rectangle(overlay, (ghost_left, ghost_top),
              (ghost_left + ghost_width, ghost_top + ghost_height),
              (0, 255, 255), 2)

cv2.namedWindow("RFF Ghost Scope", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("RFF Ghost Scope", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

print("⚡ Align your Stock Market Window inside the Ghost Box ⚡")
print("Press [Q] when ready.")

while True:
    cv2.imshow("RFF Ghost Scope", overlay)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("✅ Ghost Scope Closed")
