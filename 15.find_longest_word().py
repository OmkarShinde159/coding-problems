'''
Write a function find_longest_word()that takes a list of words and returns the length of the longest
one.

'''


def find_longest_word(list):
    list1 = []
    for i in list:
        no_of_char = 0
        for char in i:
            no_of_char += 1
        # print(no_of_char)
    list1.append(no_of_char)
    print(max(list1))
    

find_longest_word(["omkar","manish","shinde"])
