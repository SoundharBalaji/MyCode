

from tkinter import *
from tkinter import filedialog

def clickme():
    path = filedialog.askopenfilename()
    print(path)
    file = open(path,'r')
    print(file.read())

window = Tk()
button = Button(window,
                text= "click",
                command= clickme)
button.pack()
window.mainloop()