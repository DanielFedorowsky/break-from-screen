import threading
import tkinter as tk
from tkinter import messagebox


class Alerter:

    def __init__(self, title="Time to take a break", message="Time to walk around for", countdown_seconds=20):
        self.title = title
        self.message = message
        self.countdown_seconds = countdown_seconds

    def open_message_box_with_countdown(self, width=350, height=100):
        def update_countdown_label(countdown_seconds):
            countdown_label.config(text=f"{countdown_seconds} seconds left...")
            countdown_seconds -= 1
            if countdown_seconds >= 0:
                root.after(1000, update_countdown_label, countdown_seconds)
            else:
                message_box.destroy()
                root.destroy()

        root = tk.Tk()
        root.withdraw()

        x_position, y_position = _get_center_x_y(height, root, width)

        message_box = tk.Toplevel(root)
        message_box.title("Time to take a break")
        message_box.geometry(f"{width}x{height}+{x_position}+{y_position}")

        message_box.focus_force()
        message_box.bell()

        info_message = tk.Label(message_box, text=f"Time to walk around for {self.countdown_seconds} seconds",
                                font=("Arial", 14), anchor="w")
        info_message.pack(side="top", anchor="w", padx=10, pady=10)

        countdown_label = tk.Label(message_box, text="", font=("Arial", 14), anchor="w")
        countdown_label.pack(side="bottom", anchor="w", padx=10, pady=10)

        # Start the countdown in a separate thread
        countdown_thread = threading.Thread(target=update_countdown_label, args=(self.countdown_seconds,))
        countdown_thread.start()

        root.mainloop()


def _get_center_x_y(height, root, width):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2
    return x_position, y_position
