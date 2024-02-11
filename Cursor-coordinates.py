import pyautogui
import tkinter as tk


w = tk.Tk()

# Calculate the coordinates for the top-right corner of the screen
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
window_width = 200
window_height = 100
x_pos = screen_width - window_width
y_pos = 0

w.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

label = tk.Label(w, font=('Arial', 10), text="Ctrl+C to copy.")
label.pack()
coordinates = tk.Label(w, font=('Arial', 16))
coordinates.pack()


def copy(event=None):
    x, y = pyautogui.position()
    w.clipboard_clear()
    w.clipboard_append(f"{x}, {y}")

def update():
    x, y = pyautogui.position()
    text = f'x: {x}\ny: {y}'
    coordinates.config(text=text)
    w.after(100, update)
    

update()
# Set the window to be always on top
w.attributes('-topmost', True)
# Bind Ctrl+C to copy coordinates
w.bind("<Control-c>", copy)
w.mainloop()