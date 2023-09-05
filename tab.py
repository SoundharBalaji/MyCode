from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text='Tab1')
notebook.add(tab2,text='Tab2')
notebook.pack()

Label(tab1,text='Hey, You are in Tab1',height=50,width=25).pack()
Label(tab2,text='Hey, You are in Tab2 potta',height=50,width=25).pack()

window.mainloop()