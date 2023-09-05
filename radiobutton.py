from tkinter import *

window = Tk()

def click():
    if x.get() == 0:
        print("Yes, you are right ROHAN is GAYYYYYYY!")
    elif x.get() == 1:
        print("Yes, he's a little bit gay")
    elif x.get() == 2:
        print("Dai Sridhar, nee thana click panna")
    elif x.get() == 3:
        print("anime gay nanbar")

gay = ["Rohan", "Nelson", "Parthiban", "Sanjay"]
rohan = PhotoImage(file="E:\\Binary Writing\\PythonCode\\restricted.jpg")
nelson = PhotoImage(file="C:\\Users\\sound\\Pictures\\Screenshots\\Screenshot (19).png")
parthiban = PhotoImage(file="unnamed.png")
sanjay = PhotoImage(file="C:\\Users\\sound\\Downloads\\png-transparent-cartoon-animal-cartoon-animal-photography-wildlife-cartoon-thumbnail.png")

gay_photos = [rohan, nelson, parthiban, sanjay]

x = IntVar()

for index, name in enumerate(gay):
    radiobutton = Radiobutton(window,
                              text=name,
                              variable=x,
                              value=index,
                              font=("Arial", 30),
                              compound='left',
                              image=gay_photos[index],
                              command=click)
    radiobutton.pack(anchor=W)

window.mainloop()
