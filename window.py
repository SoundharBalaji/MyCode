from tkinter import *
def NewWindow():
    new_window = Toplevel() # Use Tk() to create indepdent window
    # Destroy() to close the window
window = Tk()
Button(window,
       text='New Window',
       command=NewWindow).pack()

window.mainloop()