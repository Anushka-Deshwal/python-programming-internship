import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Watch")
root.geometry("600x300")
root.configure(bg="#0f172a")
root.resizable(False, False)


def update_time():
    time_string = strftime("%H:%M:%S")
    date_string = strftime("%A, %d %B %Y")

    clock_label.config(text=time_string)
    date_label.config(text=date_string)

    root.after(1000, update_time)


# Title
title = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Poppins", 22, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
title.pack(pady=(20, 10))

# Clock Label
clock_label = tk.Label(
    root,
    font=("Courier New", 50, "bold"),
    fg="white",
    bg="#0f172a"
)
clock_label.pack()

# Date Label
date_label = tk.Label(
    root,
    font=("Poppins", 14),
    fg="#94a3b8",
    bg="#0f172a"
)
date_label.pack(pady=10)

# Start Clock
update_time()

# Run App
root.mainloop()
