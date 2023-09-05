from tkinter import *
# window

window = Tk()
window.geometry("1080x1080")
window.title("First GUI Program")
icon = PhotoImage(file='unnamed.png')
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop() # place window on screen
