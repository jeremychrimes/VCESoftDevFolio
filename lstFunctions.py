"""
<InsertNameHere> 2018
This module contains functions that will allow data to be analysed form a list.
Version: 0.2
Date Created: 2018/02/23
Date Modified: 2018/02/23

Conventions functions and variables must be prefaced with the data types they contain eg. lst, str, flt, int.
functions should be seperated by two lines.
"""


def lstSum(lst): # A function to get the sum of a list
    fltSum = float()
    for i in lst:
        fltSum = fltSum + i
    return fltSum


def lstAvg(lst): # A function to return the average of a list. DEPENDS UPON lstAvg!!
    return float(lstSum(lst)/len(lst))


def lstMin(lst): # A function to determine the minimum value in a list
    fltMinVal = float(lst[0])
    for i in lst:
        if i < fltMinVal:
            fltMinVal = i
    return fltMinVal


def lstMax(lst): # A function to determine the maximum value in a list.
    fltMaxVal = float(lst[0])
    for i in lst:
        if i > fltMaxVal:
            fltMaxVal = i
    return fltMaxVal