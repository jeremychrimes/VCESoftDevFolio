"""
<InsertNameHere> 2018
This module contains functions that will allow data to be analysed form a list.
Version: 0.1
Date Created: 2018/02/23
Date Modified: 2018/02/23
"""


def lstSum(lst):
    fltSum = float()
    for i in lst:
        fltSum = fltSum + i
    return fltSum


def lstAvg(lst):
    return float(lstSum(lst)/len(lst))


def lstMin(lst):
    fltMinVal = float(lst[0])
    for i in lst:
        if i < fltMinVal:
            fltMinVal = i
    return fltMinVal


def lstMax(lst):
    fltMaxVal = float(lst[0])
    for i in lst:
        if i > fltMaxVal:
            fltMaxVal = i
    return fltMaxVal