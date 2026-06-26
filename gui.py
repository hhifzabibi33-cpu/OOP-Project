import tkinter as tk

window = tk.Tk()

window.title("AI Classroom Noise Monitor")
window.geometry("500x300")

title = tk.Label(
    window,
    text="Classroom Noise Monitoring System",
    font=("Arial", 16)
)

title.pack(pady=20)

status = tk.Label(
    window,
    text="Noise Status: Monitoring...",
    font=("Arial", 14)
)

status.pack(pady=20)

start_button = tk.Button(
    window,
    text="Start Monitoring",
    font=("Arial", 12)
)

start_button.pack(pady=10)

window.mainloop()