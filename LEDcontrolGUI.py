#!/usr/bin/python3
from tkinter import *

canvas_width = 400
canvas_height = 300

x_center = canvas_width // 2
y_center = canvas_height // 2

radius = 50

x1 = x_center - radius
y1 = y_center - radius
x2 = x_center + radius
y2 = y_center + radius

def led_on():
    canvas.create_oval(x1, y1, x2, y2, fill = "red")
    Led_status.set("Led is ON")
    
def led_off():
    canvas.create_oval(x1, y1, x2, y2, fill = "white")
    Led_status.set("Led is ON")

window = Tk()
window.title("Control a led")

canvas = Canvas(width = canvas_width, height = canvas_height, bg = 'lightgrey')
canvas.pack()

Led_status = StringVar()
Led_status.set("Led Status")

Label(window, textvariable = Led_status).pack()

B1 = Button(text = "LED ON", command = led_on).pack()
B2 = Button(text = "LED OFF", command = led_off).pack()
B3 = Button(text = "Close", command = window.destroy).pack()

mainloop()