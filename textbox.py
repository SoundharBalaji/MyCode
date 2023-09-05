from tkinter import *
def submit():
   txt = text.get("1.0",END)
   print(txt)


window = Tk()
text = Text(window,
            )
button = Button(window,
                text ="Click",
                command= submit)
text.pack()
button.pack()

window.mainloop()