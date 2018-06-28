""" 
Jeremy Chrimes 2018 
Date Created: 2018/05/15
Date Modified: 2018/05/15
Version: 0.1

A simple selection sort algorithm
"""
def swap(lst, lowIndex, highIndex): 
	lst[highIndex], lst[lowIndex] = lst[lowIndex], lst[highIndex]

def SelectionSort(lst): 
	for parse in range(lst): 
		minValue = parse
		for i in range(parse, lst):
			if i < minValue:
    		minValue = i
  	swap(lst, minValue, parse)
  	print(lst)
	return lst


a = ['f','e','c','b','a']
SelectionSort(a)


