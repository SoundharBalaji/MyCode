def click():
    messagebox.showinfo(title="This is info box",
                        message="Sir, You are Gay!")
    messagebox.showerror(title="This is a warning box",
                           message="Caution!, person next to you is GAY!!!")

from tkinter import *
from tkinter import messagebox

window = Tk()

button = Button(window,
                text="Click me",
                command=click)
button.pack()

window.mainloop()