from tkinter import *


#set up basic tk GUI size and background color
root = Tk()
root.resizable(0,0)
root.title("list of friends age's")



#arrAgess
arrAges=[]
arrOutputAge=[]



def Output_Display():
    
    intAge=(entAge.get())

    intOutputAges = (entAge.get())

    intAge=int(intAge)


    arrOutputAge.append(intOutputAges)
    word = " ".join(arrOutputAge)

    arrAges.append(intAge)

    total=sum(arrAges)

    length=len(arrAges)

    av = total/length
    av = ('%.2f' % av)

    Average_lbl.configure(text = av)
    numAgeLbl.configure(text = length)
    intOutputAgesLbl.configure(text=word)


def funcErrorhandling():
    print("empty function")

def funcAgeArray():
    print("empty function")


def funcAgeListDisplay():
    print("empty function")

def funcAvgcalculator():
    print("empty function")

def funcHighestAge():
    print("empty function")

def funcLowestAge():
    print("empty function")

#GUI Widgets for tkinter


w=Label(root, text="Age recorder", font=('Verdana', 28) )
w.grid(row=0, column=0, columnspan=2,pady=2, ipady=2, padx=60)

w=Label(root, text="Enter the Ages for each game", font=('Verdana', 12, 'italic') )
w.grid(row=1, column=0, columnspan=2, sticky=N )

w=Label(root, text="Age", font=('Arial', 14) )
w.grid(row=2, column=0, sticky=SE, padx=45, pady=0)

bw=Label(root, text="")
bw.grid(row=2, column=1, sticky=SW, padx=45, pady=10)

#text box to enter runs per game
entAge=Entry(root, width=4,  )
entAge.grid(row=3, column=0, sticky=E, padx=45)

#button for submitting runs per game
btnSubmit=Button(root, text="Submit", font=('Arial', 14), relief=RAISED, command = Output_Display)  #Main function is called here - call a function for when the button is pressed
btnSubmit.grid(row=3, column=1, sticky=W)

w=Label(root, text="Total of Ages", font=('Arial', 16) )
w.grid(row=4, column=0, sticky=E, padx=45, pady=15)

numAgeLbl=Label(root, text="6", font=('Arial', 16) )
numAgeLbl.grid(row=4, column=1, sticky=W)

w=Label(root, text="List of Ages", font=('Arial', 16) )
w.grid(row=5, column=0, sticky=E, padx=45)

Average_Age=Label(root, text="Average Age", font=('Arial', 16) )
Average_Age.grid(row=5, column=1, sticky=W, padx=0)

intOutputAgesLbl=Label(root, text="", font=('Arial', 14) )
intOutputAgesLbl.grid(row=6, column=0, sticky=E, padx=45)

Average_lbl=Label(root, text="23.45", font=('Arial', 14) )
Average_lbl.grid(row=6, column=1, sticky=NW)

bw=Label(root, text="")
bw.grid(row=7, column=1, sticky=SW, padx=45, pady=1)

root.mainloop()
