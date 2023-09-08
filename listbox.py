def order():
    print("Your Ordered:")
    selected = menu.curselection()
    item=(menu.get(selected))
    print(item)

from tkinter import *

window = Tk()

window.title("HOTEL MENU")

menu = Listbox(window,
               bg="Yellow",
               fg="red",
               font=("Freestyle Script",60))
menu.pack()

menu.insert(1,"Idly")
menu.insert(2,"Dosa")
menu.insert(3,"Parotta")
menu.insert(4,"Chapati")
menu.insert(5,"Theriyathu")

submit_button = Button(text="Submit",
                       fg="red",
                       bg="yellow",
                       command=order)
submit_button.pack()

menu.config(height=menu.size())

window.mainloop()