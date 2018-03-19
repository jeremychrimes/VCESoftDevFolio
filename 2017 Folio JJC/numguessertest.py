# Jeremy Chrimes <jeremy.chrimes@gmail.com>
# Last modified: 2017/08/13
# Version: 0.1

# This program will log the ammount of guesses that are needed to find a certain number
# This program works best in either bash or powershell though it can be ran in idle. 
# The file numguess.py needs to be stored in the same directory otherwise the program will not run.



from numguess import numGuess # Importing the number guesser class
from sys import exit
setup = False
while (setup == False): 
    low = input("Low level: ")
    high = input("High level: ")
    guesser = list()
    finishList = list() 
    outputFile = input("Where would you like to output this file (~/a.out): ")
    if (outputFile == "") : 
        outputFile = "a.out"
    File = open(outputFile, "w")
    print("The program will write to {0}. The high value of the test will be {1} and the low value will be {2}".format(outputFile, high, low))
    Check = input("Is this ok (Y/N) ")
    if (Check.upper() == "Y") :
        print ("The program will now run") 
        high = int(high)
        low = int(low)
        runapp = True
        setup = True
if (runapp == True): 
    for zed in range (int(low + 1 ), int(high + 1 )): 
        print (zed)
        guesser.append(numGuess(high, low))
        gn = len(guesser) - 1
        record = list()
        record.append(guesser[gn].midpoint)
        timesRan = int(1)
        while (guesser[gn].midpoint != zed): 
            if (zed < guesser[gn].midpoint) :
                guesser[gn].valueLower()
                record.append(guesser[gn].midpoint)
                timesRan += 1 
                
            if (zed > guesser[gn].midpoint) : 
                guesser[gn].valueHigher()
                record.append(guesser[gn].midpoint)
                timesRan += 1 
        print ("{0},{1}".format(str(zed),str(timesRan)))
        File.write("{0},{1}\n".format(str(zed),str(timesRan)))
