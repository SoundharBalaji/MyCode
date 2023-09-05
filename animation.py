from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xvelocity = 1
yvelocity = 1

def move_rohan():
    canvas.move(rohan, xvelocity, yvelocity)
    coordinate = canvas.coords(rohan)
    print(coordinate)
    window.after(10, move_rohan)  # Call move_rohan() every 10 milliseconds

window = Tk()
window.title("Flying Gay")

canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

rohan_img = PhotoImage(file="C:\\Users\\sound\\Pictures\\pyscho.png")
rohan = canvas.create_image(0, 0, image=rohan_img, anchor=NW)

move_rohan()  # Start the animation loop

window.mainloop()
