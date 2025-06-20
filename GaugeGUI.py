#!/usr/bin/python3
from tkinter import *
import math
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text = current_time)
    window.after(1000, update_time)

def update_gauge(value):
    canvas.delete("needle")
    angle = -135 + (value / 1000) * 270 
    angle_rad = math.radians(angle)

    x_end = center_x + needle_length * math.cos(angle_rad)
    y_end = center_y + needle_length * math.sin(angle_rad)

    canvas.create_line(center_x, center_y, x_end, y_end, fill="red", width=3, tag="needle")
    value_label.config(text=str(value))

window = Tk()
window.title("Gauge")

Label(window, text="Time:").grid(row=0, column=0)
time_label = Label(window, font=("Courier", 18), width=10, bg="lightgray")
time_label.grid(row=1, column=0, padx=10)


canvas_width = 300
canvas_height = 300
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.grid(row=0, column=1, rowspan=4)

center_x = canvas_width // 2
center_y = canvas_height // 2
radius = 120
needle_length = 100

for i in range(0, 1001, 100):
    angle = -135 + (i / 1000) * 270
    angle_rad = math.radians(angle)
    x_outer = center_x + radius * math.cos(angle_rad)
    y_outer = center_y + radius * math.sin(angle_rad)
    x_inner = center_x + (radius - 15) * math.cos(angle_rad)
    y_inner = center_y + (radius - 15) * math.sin(angle_rad)
    canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)
    x_text = center_x + (radius - 30) * math.cos(angle_rad)
    y_text = center_y + (radius - 30) * math.sin(angle_rad)
    canvas.create_text(x_text, y_text, text=str(i), font=("Arial", 8))


canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, fill="gray")


value_label = Label(window, text="0", font=("Arial", 24))
value_label.grid(row=4, column=1)


value = 0
def simulate():
    global value
    value = (value + 50) % 1001
    update_gauge(value)
    window.after(1000, simulate)


update_time()
simulate()
window.mainloop()