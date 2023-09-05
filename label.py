from tkinter import *

window = Tk()

photo = PhotoImage(file="unnamed.png")
label = Label(window,
              text= "Hi Bro ,\nWhy are you gay?",
              font=("Arial",90,"bold"),
              fg = "green",
              bg= "black",
              relief= RAISED,
              bd= 50,
              padx= 10,
              pady=10,
              image= photo,
              compound= "bottom"
              )
label.pack()

window.mainloop()