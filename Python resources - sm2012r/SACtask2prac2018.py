from tkinter import *


#set up basic tk GUI size and background color
root = Tk() # Initialise the window
root.configure(background="lime green") # Set the background colour to be lime green
root.resizable(0,0) # Set the window to be non resizable 
root.title("list of friends age's") # Set the title of the window to be list of friends



#arrAgess
arrAges=[] # Create an array of ages
arrOutputAge=[] # Create an array of output ages 



def Output_Display():
    
    intAge=(entAge.get()) 
    intAge=int(intAge)
    funcAgeArray(intAge)
    funcAgeListDisplay(intAge)
    funcAvgcalculator(intAge)
    funcHighestAge()
    funcLowestAge()
def Output_Display_Event(event): 
    Output_Display()
    

def funcErrorhandling():
    #print("empty function")

def funcAgeArray(newAge):
    #print("empty function")
    arrAges.append(newAge)


def funcAgeListDisplay(newAge):
    # print("empty function")
    intOutputAges = (entAge.get()) # 
    arrOutputAge.append(intOutputAges)
    word = " ".join(arrOutputAge)
    intOutputAgesLbl.configure(text=word)
    

def funcAvgcalculator(newAge):
    #print("empty function")
    #arrAges.append(newAge) 

    total=sum(arrAges) # Get a sum of the array

    length=len(arrAges) # Get the length of the array

    av = total/length # calculate the mean by using total over lenght
    av = ('%.2f' % av) # Set the average to use only 2 decimal places
    numAgeLbl.configure(text = length) # Set the length label
    Average_lbl.configure(text = av) # Set the average label

def funcHighestAge():
    #print("empty function")
    intMaxVal = int(arrAges[0])
    for i in arrAges:
        if (i > intMaxVal):
            intMaxVal = i
    high_lbl.configure(text="High: {}".format(intMaxVal))

def funcLowestAge():
    #print("empty function")
    intMinVal = int(arrAges[0])
    for i in arrAges:
        if (i < intMinVal):
            intMinVal = i
    low_lbl.configure(text="Low: {}".format(intMinVal))

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
entAge.bind('<Return>', Output_Display_Event)
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

low_lbl = Label(root, text='Low: 0', font=("Arial",14))
low_lbl.grid(row=7, column=0, sticky=SW, padx=5, pady=5)

high_lbl = Label(root, text='High: 0', font=("Arial",14))
high_lbl.grid(row=7, column=1, sticky=SE, padx=5, pady=5)




root.mainloop()
