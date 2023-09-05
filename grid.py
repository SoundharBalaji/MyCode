def show():

    print(NameEntry,DeptEntry,EmailEntry)

from tkinter import *
window = Tk()

NameLabel = Label(window,text='Name:').grid(row=0,column=0)
NameEntry = Entry().grid(row=0,column=1)

DeptLabel = Label(window,text='Dept:').grid(row=1,column=0)
DeptEntry = Entry().grid(row=1,column=1)

EmailLabel = Label(window,text='Email Address:').grid(row=2,column=0)
EmailEntry = Entry().grid(row=2,column=1)

submit = Button(window,text='Submit',command=show)
submit.grid(row=3,column=0,columnspan=2)

window.mainloop()