import tkinter as tk
import random


window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

x = 300
y = 200

point = canvas.create_oval(x, y, x + 4, y + 4)


def move():
    global x, y

    dx, dy = random.choice([
        (10, 0),
        (-10, 0),
        (0, 10),
        (0, -10)
    ])

    x += dx
    y += dy

    canvas.coords(point, x, y, x + 4, y + 4)

    window.after(50, move)


move()

window.mainloop()