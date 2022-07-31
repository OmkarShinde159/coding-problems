'''
Write a function find_longest_word()that takes a list of words and returns the length of the longest
one. Use only higher order functions.
'''

def longest(list):
    x = [len(x) for x in list]
    # x = max(x)
    print("The longest length of string is:", max(x))

list = ['om','python','developer','12345',"omicron"]
longest(list)


