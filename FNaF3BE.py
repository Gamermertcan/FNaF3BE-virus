import tkinter as tk
import random

def move_window(window):
    window.update()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    new_x = random.randint(0, screen_width - window_width)
    new_y = random.randint(0, screen_height - window_height)
    window.geometry(f"+{new_x}+{new_y}")
    window.after(100, lambda: move_window(window))

def clone_window(parent_window):
    for _ in range(6):
        new_window = tk.Tk()
        new_window.title('You Got "Hey Stinky\'d"')
        tk.Label(new_window, text='Hey Stinky!', font=("Arial", 48)).pack()
        new_window.bind("<Button-1>", lambda e: clone_window(new_window))
        move_window(new_window)
        new_window.mainloop()

def close_initial():
    R.destroy()
    LOL = tk.Tk()
    LOL.title('You Got "Hey Stinky\'d"')
    tk.Label(LOL, text='Hey Stinky!', font=("Arial", 48)).pack()
    LOL.bind("<Button-1>", lambda e: clone_window(LOL))
    move_window(LOL)
    LOL.mainloop()

R = tk.Tk()
R.title('Five Nights at Freddy\'s 3 Beginner Edition | Loading')
R.after(3000, close_initial)
R.mainloop()