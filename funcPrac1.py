def lstSum(lst):  # A function to get the sum of a list
    intSum = int()
    for i in lst:
        intSum = intSum + i
    return intSum


def lstAvg(lst):  # A function to return the average of a list. DEPENDS UPON lstAvg!!
    return int(lstSum(lst)/len(lst)) # divide the sum of the list by the


def __main__ () :
    lst = list()
    for i in range(3):
        lst.append(int(input("Number {}: ".format(i))))
    intAddTotal = lstSum(lst)
    intAvg = lstAvg(lst)
    print(intAvg)
__main__()