from tkinter import *


#set up basic tk GUI size and background color
root = Tk()
root.resizable(0,0)
root.title("Run Calculator")

#global variable arrays
arrRuns=[]          #to make list of runs (for total, max, and min calculations. Must be int type)
arrOutputRuns=[]     #to output list to GUI

#Define functions.

# the output_display function acts as the main function. It mostly calls other functions (like all good  main functions)
#This gets called from within tkinter when the submit button is pressed. (see "btnSubmit" in tkinter code)

def Output_Display():

    intRuns=(entRuns.get())         #Get value from Runs entry box. initially string type but must be converted
    #boolCheckOk = True
    boolIntCheck = funcIntegerCheck(intRuns)    #check for integer

    if (boolIntCheck == True):      #error check 1
        boolPosNumCheck = funcPositiveNumCheck(int(intRuns))
    #else:
        #funcPopoupError()

        if (boolPosNumCheck == True):           #error check 2
            funcRunListDisplay(intRuns)   #call function to add display list
            intRuns=int(intRuns)      #convert Run string to integer

            funcRunArray(intRuns)    #call function to fill list

            funcAvgcalculator(arrRuns)       #call function to find avg - send the array of Runs to the function

            funcMaxAndMin(arrRuns)           #call function to find max - send the array of Runs to the function
        else:
            funcPopoupError()

    else:
        funcPopoupError()


def funcPopoupError():
    popup = Toplevel(root)
    popup.wm_title("Error!")
    popup.tkraise(root)

    lblErrMsg = Label(popup, text="Please enter a positive whole number", font=('Verdana', 28) )
    lblErrMsg.grid(row=0, column=0, columnspan=2,pady=2, ipady=2, padx=60)
    btnExit = Button(popup, text = "OK",command = popup.destroy)
    btnExit.grid(row=3, column=0)


"""accepts a value from the user and outputs an error message if
an integer (whole number) is not entered.    """
def funcIntegerCheck(num):
    try:
        num = int(num)
        print("intger")
        return True
    except ValueError as description :
        print (str (description) )              # system error message, useful for debugging but shouldn't appear in your programs
        print ( "Thats not an integer" )        # programmer error message that user will understand
        return False

"""accepts a value from the user and outputs an error message if
a negative number is entered.    """
def funcPositiveNumCheck(num):
    if (num >=0):
        print ("true")
        return True
    else:
        print("dsfgds")
        return False



#Fill the array with run scores
def funcRunArray(intArrayNum):
    arrRuns.append(intArrayNum)

#Format array for printing to the GUI
def funcRunListDisplay(intOutputRuns):
    arrOutputRuns.append(intOutputRuns)
    word = " ".join(arrOutputRuns)
    intOutputRunsLbl.configure(text=word)

def funcAvgcalculator(addends):
    intTotal=sum(addends)          #find the sum of all numbers in array
    intLength=len(addends)         #find the number of addends in array
    floAverage = intTotal/intLength   #find average
    floAverage = ('%.2f' % floAverage)  #set average to 2 decimal places

    Average_lbl.configure(text = floAverage)    #print averRun to screen
    numRunsLbl.configure(text = intLength)       #print length of array (num of Runs) to screen

#finds the maximum and minimum number from the elements in an array
def funcMaxAndMin(intElements):
    intMax = 0
    for i in intElements:
        if i > intMax:
            intMax = i
    print (intMax)
    lblMaxRunnum.configure(text = intMax)




#GUI Widgets for tkinter


w=Label(root, text="Runs recorder", font=('Verdana', 28) )
w.grid(row=0, column=0, columnspan=2,pady=2, ipady=2, padx=60)

w=Label(root, text="Enter the Runs for each game", font=('Verdana', 12, 'italic') )
w.grid(row=1, column=0, columnspan=2, sticky=N )

w=Label(root, text="Runs", font=('Arial', 14) )
w.grid(row=2, column=0, sticky=SE, padx=45, pady=0)

bw=Label(root, text="")
bw.grid(row=2, column=1, sticky=SW, padx=45, pady=10)

#text box to enter runs per game
entRuns=Entry(root, width=4,  )
entRuns.grid(row=3, column=0, sticky=E, padx=45)

#button for submitting runs per game
btnSubmit=Button(root, text="Submit", font=('Arial', 14), relief=RAISED, command = Output_Display)  #Main function is called here - call a function for when the button is pressed
btnSubmit.grid(row=3, column=1, sticky=W)

w=Label(root, text="Total Runs", font=('Arial', 16) )
w.grid(row=4, column=0, sticky=E, padx=45, pady=15)

numRunsLbl=Label(root, text="6", font=('Arial', 16) )
numRunsLbl.grid(row=4, column=1, sticky=W)

w=Label(root, text="List of Runs", font=('Arial', 16) )
w.grid(row=5, column=0, sticky=E, padx=45)

Average_Age=Label(root, text="Average Runs", font=('Arial', 16) )
Average_Age.grid(row=5, column=1, sticky=W, padx=0)

intOutputRunsLbl=Label(root, text="", font=('Arial', 14) )
intOutputRunsLbl.grid(row=6, column=0, sticky=E, padx=45)

Average_lbl=Label(root, text="23.45", font=('Arial', 14) )
Average_lbl.grid(row=6, column=1, sticky=NW)

bw=Label(root, text="")
bw.grid(row=7, column=1, sticky=SW, padx=45, pady=1)

# labels for max num
lblMaxRuntxt=Label(root, text="Highest Age", font=('Arial', 16) )    #set up label
lblMaxRuntxt.grid(row=8, column=0, sticky=E)                  #location of label
lblMaxRunnum=Label(root, text=" ", font=('Arial', 16) )    #set up label
lblMaxRunnum.grid(row=9, column=0, sticky=E)                  #location of label


#button for submitting runs per game
btnSubmit=Button(root, text="Submit", font=('Arial', 14), relief=RAISED, command = Output_Display)  #Main function is called here - call a function for when the button is pressed
btnSubmit.grid(row=3, column=1, sticky=W)

lblMaxRuntxt=Label(root, text="Highest Age", font=('Arial', 16) )    #set up label
lblMaxRuntxt.grid(row=8, column=0, sticky=E)                  #location of label

root.mainloop()
