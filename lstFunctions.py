"""
<InsertNameHere> 2018
This module contains functions that will allow data to be analysed form a list.
Version: 0.2
Date Created: 2018/02/23
Date Modified: 2018/02/23

Conventions functions and variables must be prefaced with the data types they contain eg. lst, str, flt, int.
functions should be seperated by two lines.
"""


def lstSum(lst):  # A function to get the sum of a list
    intSum = int()
    for i in lst:
        intSum = intSum + i
    return intSum


def lstAvg(lst):  # A function to return the average of a list. DEPENDS UPON lstAvg!!
    return int(lstSum(lst)/len(lst)) # divide the sum of the list by the


def lstMax(lst):  # A function to determine the maximum value in a list.
    intMaxVal = int(lst[0])
    for i in lst:
        if i > intMaxVal:
            intMaxVal = i
    return intMaxVal


def lstLinearFind(item, lst):
    for index, content in enumerate(lst): ## Get the list item and key until the list ends.
        # print("{0}:{1}".format(index,item))#Debug to test list is being enumerated properly
        if content == item:
            return index

def lstMin(lst): # A function to determine the minimum value in a list
    fltMinVal = float(lst[0])
    for i in lst:
        if i < fltMinVal:
            fltMinVal = i
    return fltMinVal


