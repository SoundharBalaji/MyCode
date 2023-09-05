from tkinter import *

def submit():
    username =  entrybox.get()
    print("Poda mental "+username)

def delete():
    entrybox.delete(0, END)

def backspace():
    entrybox.delete(0)

window = Tk()

window.title("Enter your name")

entrybox = Entry(window,
                 font= ("Eras Bold ITC",25),
                 bg="black",
                 fg="green",
                 show="$")

entrybox.pack(side=LEFT)

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="Remove",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()
