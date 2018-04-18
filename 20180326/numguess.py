## Jezz Chrimes <jjchr2@schools.vic.edu.au>
# Last modified: 2017/08/13
# Version: 0.1

# This class is a model for guessing numbers. It is a requirement for both cliguesser.py and numguessertest.py.

from random import randint
class numGuess: 
    def __init__ (self, High, Low): # When initilising the class you need to provide a interger high value and low value. 
        self.highValue = High #Setting the high value that will be used through out the use of the program
        self.high = High 
        self.lowValue = Low
        self.low = Low 
        self.midpoint = self.getMidpoint()
        # print (self.midpoint) # This print command is for debuging purposes to make sure that the program works as intended. 
    def getMidpoint (self): 
        return round((self.highValue + self.lowValue) / 2)
    def valueHigher(self): 
        self.lowValue = self.midpoint
        self.midpoint = self.getMidpoint() 
        return self.getTuple()
    def valueLower(self) :
        self.highValue = self.midpoint
        self.midpoint = self.getMidpoint()
        return self.getTuple()
    def getTuple(self):
        return (self.midpoint, self.lowValue, self.highValue)
