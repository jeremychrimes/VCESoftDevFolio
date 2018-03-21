## Jezz Chrimes <jjchr2@schools.vic.edu.au>
# Last modified: 2017/08/13
# Version: 0.1

# This program will provide a command line interface for the number guesser.

# The file numguess.py needs to be stored in the same directory otherwise the program will not run.
# In future this code should have the functionality that the users can choose the low and high parameter.


from numguess import numGuess


guesser = numGuess(100, 0) # Run the initiliser of the class
running = True # Creates a variable that is true while the application is running
while (running == True):
    print (guesser.getTuple())
    userInput = input("Is your number higher or lower? (H/L/Q) ")
    if (userInput.upper() == "H"):
        guesser.valueHigher()
        print(guesser.midpoint)
    elif (userInput.upper() == "L"):
        guesser.valueLower()
        print (guesser.midpoint)
    elif(userInput == "Q") :
        running = False
        print("Thank you for using Number Guesser")
    else:
        print ("Invalid input")
