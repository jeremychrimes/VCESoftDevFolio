# Exam Percentage Generator
# Jeremy Chrimes 2017
# This function checks a interger value to make sure that it is valid

# This function uses an if else if statement to work out what a persons grade is based upon their percentage. Note it will not work if the percentage is over 100%.
def generateGrade(percentage) :
    if (percentage <= 100) :
        if (percentage >= 90) :
            return (True, "A+")
        elif (percentage >= 80):
            return(True, "A")
        elif (percentage >= 75):
            return (True, "B+")
        elif (percentage >= 70):
            return (True, "B")
        elif (percentage >= 65):
            return (True, "C+")
        elif (percentage >= 60):
            return (True, "C")
        elif (percentage >= 55):
            return (True, "D+")
        elif (percentage >= 50):
            return (True, "D")
        elif (percentage >= 45):
            return (True, "E")
        else:
            return (True, "N")
    else :
        return (False, "Please enter a percentage")

def askUser(testMarks):
    try : ##Test that the user has inputed a float number
        testScore = input("What did you score on the test") ## Ask User what they scored on the test
        float(testScore) ## Check it is a float
    except :
        print("Error: Please input a number") ## If it gets an error it is not a float and will print an error.
        return 0 ## Break the function by returning 0
    if (
while True:
    askUser(0)

