from tkinter import messagebox

class AlertSystem:

    def show_alert(self):

        messagebox.showwarning(
            "Noise Alert",
            "Classroom noise level is HIGH!"
        )