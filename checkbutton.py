from tkinter import *

def show():
    if x.get()==1:
        print("Otha nee matikina")
    else:
        print("Dae potta agree pannu da!")

window = Tk()
x= IntVar()
photo = PhotoImage(file="unnamed.png")

check_button = Checkbutton(window,
                           text= "I agree to new terms & condition",
                           variable= x,
                           onvalue= 1,
                           offvalue= 0,
                           command=show,
                           image= photo,
                           compound=LEFT)

check_button.pack()
window.mainloop()