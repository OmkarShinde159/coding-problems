'''
Using the higher order function reduce(), write a function max_in_list()that takes a list of numbers
and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
call the reduce()function directly?
'''

import functools

def max_in_list(list):
    # lets find sum also
    print(functools.reduce(lambda a,b : a+b, list ))
    # max of three
    print(functools.reduce(lambda a,b:a if a>b else b, list))
    # min of list
    print(functools.reduce(lambda a,b : a-b, list ))

list = [1,2,5,10,78,2]
max_in_list(list)



