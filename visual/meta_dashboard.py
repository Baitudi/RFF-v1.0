
import tkinter as tk
import os

FEEDBACK_PATH = "models/meta/engine_feedback.txt"

def load_feedback():
    if not os.path.exists(FEEDBACK_PATH):
        return "[Meta] Feedback file not found."
    with open(FEEDBACK_PATH, "r") as f:
        return f.read()

def refresh_text():
    feedback = load_feedback()
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, feedback)

root = tk.Tk()
root.title("RFF Meta Feedback Dashboard")
root.geometry("500x400")

text_display = tk.Text(root, wrap=tk.WORD, font=("Courier", 10), bg="#1e1e1e", fg="#00ffcc")
text_display.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

refresh_btn = tk.Button(root, text="Refresh Report", command=refresh_text, bg="#444", fg="#fff")
refresh_btn.pack(pady=10)

refresh_text()
root.mainloop()
