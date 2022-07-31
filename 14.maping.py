'''
Write a program that maps a list of words into a list of integers representing the lengths of the correponding
words.
'''

list_of_words = ["apple","banana","cherry"]     # access word in list
list_of_int = [len("apple"),len("banana"), len("cherry")]  # access chars in word
print(list_of_words)
print(list_of_int)



def mapList(list):
    list1 = []
    for i in list:
        no_of_char = 0
        for char in i:
            no_of_char += 1
        list1.append(no_of_char)
    print(list1)

mapList(["apple","banana","cherry"])


def mapList(x):
    return list(map(lambda x: len(x),x))

print(mapList(["apple","banana","cherry"]))