def click():
    while True:
        messagebox.showwarning(title="This is a warning box",
                           message="Virus found !!!")

from tkinter import *
from tkinter import messagebox

window = Tk()

button = Button(window,
                text="Click me",
                command=click)
button.pack()

window.mainloop()