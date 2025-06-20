#!/usr/bin/python3
from tkinter import *

def factorial():
    result = 1
    try:
        num = int(e.get())
        for i in range(1, num + 1):
            result *= i
        factorial_result.set(result)
        
    except ValueError:
        factorial_result.set("Invalid")

window = Tk()
window.title("Calculate factorial")

Label(window, text = "Enter an integer: ").grid(row = 0, column = 0)

e = Entry(window)
e.grid(row = 0, column = 1)

button = Button(window, text = 'Factorial', command = factorial).grid(row = 2, column = 1)

factorial_result = StringVar()
factorial_result.set("Result")
Label(window, textvariable = factorial_result).grid(row=1, column=1)

mainloop()