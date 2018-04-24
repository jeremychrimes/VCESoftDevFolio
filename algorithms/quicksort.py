"""
Jeremy Chrimes  2018 

Date created: 
Date modified: 
Version: 

This is a quick module to complete a quick sort. 
"""

def quickSort(lst, start, end): 
	if start < end: 
		# Split the list. 
		pivot = partition(lst, start, end)

		# Sort both sides
		