'''
Write a function filter_long_words()that takes a list of words and an integer n and returns the list of
words that are longer than n.
'''
list = ["Om","Ram","sai","shiv"]
n = 3
def longerWords(list,n):
    longList = []
    for char in list:
        if len(char) > n:
            longList.append(char)
    return longList

list = ["Om","Ram","sai","shiv","Samiksha","mango"]
n = 3
print(longerWords(list,n))
