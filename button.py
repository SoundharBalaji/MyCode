from tkinter import *
def msg():
    print("You are gay!")
window = Tk()

button = Button(window,
                text="click here",
                font=("Bahnschrift Light SemiCondensed",25),
                command= msg,
                bg="black",
                fg="green")

button.pack()

window.mainloop()