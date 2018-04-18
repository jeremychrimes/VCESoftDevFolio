"""
Jeremy Chrimes 2018

Version: 0.1
Date Created: 2018/04/14
Date Modified: 2018/04/14

A Program to figure out the algorithm for the sort in Chrimesy DB with the test dictionary.
{1: {name: Jeremy, age: 17}, 2: {name: William, age: 15}, 2: {name: Jonathan, age: 45}}
"""


People = {1: {"name": "Jeremy", "age": 17}, 2: {"name": 'William', 'age': 15}, 3: {'name': 'Jonathan', 'age': 45}}

def getKey(dictionary, prop):
    tempLst = list()
    for key, obj in dictionary.items():
        tempLst.append([key,obj[prop]])
    return tempLst





