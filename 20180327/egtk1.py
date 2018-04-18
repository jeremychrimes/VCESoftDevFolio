import tkinter # import the tkinter moduel

def main(): # This is the main function of the program
    root = tkinter.Tk() # Initialise the Tkinter Class
    myWindow = tkinter.Canvas(root, width=100, height=100) # Name you canvas myWindow and set the size to 100 x 100
    myWindow.pack()
    myWindow.bind("<Button-1>", testClick) # Bind window to button 1 and if it is clicked run action test event
    root.mainloop() # Run the main loop


def testClick(event): #Define the test class event
    print("Clicked at: {0}, {1}".format(event.x, event.y)) #Define the test click event handler

main()