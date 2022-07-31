
'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding
words. Write it in three different ways: 1) using a for­loop, 2) using the higher order function map(), and 3)
using list comprehensions
'''

# list = ["apple","banana","cherry"] input
# list = [5,6,6] output


def returnLength(list):
    newList = []
    for i in list:
        newList.append(len(i))
    return newList
    
lis = ["apple","banana","cherry"]
print(returnLength(lis))



def returnLength(list):
    newlist = [len(i) for i in list]
    return newlist

val = ["apple","banana","cherry"]
print(returnLength(val))


def findlen(a):
    return len(a)

fruits = ['apple', 'banana', 'cherry']
res = list(map(findlen , fruits))
print(res)

