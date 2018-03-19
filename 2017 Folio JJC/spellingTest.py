## Jeremy Chrimes <jeremy.chrimes@gmail.com>
## Speelling test practice 0.1
## This script will alow users to practice a spelling test. The wordlist must be in the form of an array and can be loaded from a text (txt) file.

from random import randint
from time import sleep
fileName = str() ## Defining a variable for the file name
wordList = list() ## Creating a list for the words that will be imported from the wordlistfile.
appDictionary = list()
spellingTestRan = False
waitTime = int(5)
File = open("tmp.txt", "r+")
print ("Welcome to spelling test version 0.1")

def getWordList () -> list: # Create a module to load file 
    fileName = input ("What is the name of your file? ") ## Ask the user the file name.
    if (fileName == "") : 
        fileName = "tmp.txt"
    try: 
        File = open(fileName, "r+") ## Loading the file into the application.
        wordList = list(str(File.read()).split(", ")) ## Converting the wordlist to a string to use the delimiter and make a list from this. 
        print(wordList) ## Debug to confirm that the wordlist has been created.
        print ("Your wordlist {0} has been succuesfully imported".format(fileName))
        return wordList
    except:
        print("There was an issue importing the file, Please try again")
def formatWordList ():
    print ("Testing WordList") ##Output to the user to let them know that it is testing th
    # print(wordList) ## Debug: Pring the wordlist.
    try: 
        for i in range(len(wordList)) : ## Create a for loop to create the application array
            appDictionary.append(dict([("Word",wordList[i]),("complete",False),("Spelling","")])) ## Append the word to the appDictionary and set the value of the rating to 0 
            # print(appDictionary[i]) ## Debug: Print the dictionary object to make sure that it was appended.
    except:
        print ("There was an error creating the application array please try again")
def speellingTest ():
    for wordNum in range(len(appDictionary)):
        print("\r" + "{0}".format(appDictionary[wordNum]["Word"]),end="")
        sleep(5)
        wordLen = len(appDictionary[wordNum]["Word"]) # Create a variable to get the word's length in order to hide it. 
        # print(wordLen) ##Debug: print the word's length
        lineClear = (" " * wordLen) ## Print spaces over the word to help to hide it. 
        # print(lineClear)
        userWord = input("\r{}".format(lineClear) + "\r > ") ## Input field for the user to input their spelling of the word
        if (userWord == appDictionary[wordNum]["Word"]): ## Check if the word is the same as the word in the word list. 
            appDictionary[wordNum]["complete"] = True ## Set the `complete` varible in the words object in the appDictionary to be True
            print("Correct") ## Print Correct
        else:
            appDictionary[wordNum]["Spelling"] = userWord
    
def getResults():
    correct = 0
    incorect = int()
    correctWords = list()
    incorectWords = list() 
    for wordNum in range(len(appDictionary)):
        # print(appDictionary[wordNum]["complete"]) ##Debug: Test that the methord is working correctly 
        if (appDictionary[wordNum]["complete"] == True):
            correct += 1
        elif (appDictionary[wordNum]["complete"] == False):
            incorect += 1
    print ("{0} words were correct. {1} words were spelt incorrectly".format(correct, incorect))
def createReport():
    outputFilename = input ("Where would you like to export your work: ")
    File = open(outputFilename, "w")
    for wordNum in range (len(appDictionary)):
        obj = appDictionary[wordNum]
        output = "{0},{1},{2}\n".format(obj["Word"],obj["complete"],obj["Spelling"])
        File.write(output)
        
                
                
wordList = getWordList()
formatWordList()
# print(appDictionary) ##DEBUG: Print the dictionary to confirm it has been created. 
speellingTest() 
getResults()
createReport()
input()
