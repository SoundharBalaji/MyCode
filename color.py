from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    print(color)
    hexValue = color[1]
    window.config(bg=hexValue)

window = Tk()
window.geometry("1080x1080")
button = Button(window,
                text="Click me",
                command=click)
button.pack()
window.mainloop()