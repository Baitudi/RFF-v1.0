import cv2

def draw_accuracy_score(frame, total, correct):
    accuracy = int((correct / total) * 100) if total > 0 else 0
    text = f"AI Accuracy: {accuracy}%"
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    return frame
