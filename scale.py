print("Now play a gay test meter")
from tkinter import *

def submit():
    if i.get()==0:
        print("It's Soundhar Balaji")
    elif i.get()==1:
        print("somesh")
    elif i.get()==2:
        print("suriya")
    elif i.get()==3:
        print("Michael")
    elif i.get()==4:
        print("parthiban")
    elif i.get()==5:
        print("Seran")
    elif i.get()==6:
        print("Sanjay")
    elif i.get()==7:
        print("pugazh")
    elif i.get()==8:
        print("Nelson")
    elif i.get()==9:
        print("Ithu Sridhar")
    else:
        print("Ithu Namma ROHANSHAJ endra gayshaj")


window = Tk()
i = IntVar()

window.title("Gay Meter")

sigma = PhotoImage(file="C:\\Users\\sound\\Downloads\\png-clipart-christian-bale-american-psycho-patrick-bateman-hollywood-film-christian-bale-celebrities-microphone-thumbnail.png")
sigmalabel = Label(image=sigma)
sigmalabel.pack()

gay_scale = Scale(window,
                  from_= 0,
                  to= 10,
                  variable= i,
                  length=1000,
                  font=("Arial",30),
                  tickinterval=1,
                  orient="vertical",
                  showvalue=0,
                  troughcolor="White",
                  width=5)
gay_scale.pack()

rohan = PhotoImage(file="C:\\Users\\sound\\Pictures\\pyscho.png")
gaylabel = Label(image=rohan)
gaylabel.pack()


submit_button = Button(window,
                       text= "Submit",
                       command= submit)
submit_button.pack()

window.mainloop()