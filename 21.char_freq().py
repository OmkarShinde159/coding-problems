'''
Write a function char_freq()that takes a string and builds a frequency listing of the characters contained
in it. Represent the frequency listing as a Python dictionary. Try it with something like
char_freq("abbabcbdbabdbdbabababcbcbab").
'''
# function 
# string input
# what function does: builds a frequency listing
# frequency of what? characters present in string input
# what is frequency listing ?
# represent as python dict means key:value format


# method 1
def char_freq(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else: 
            freq[i] = 1
    print(str(freq)) 

string = "aabbbccccd"
char_freq(string)

# method 2
from collections import Counter

def char_freq(string):
    new = Counter(string)
    print(str(new))

# char_freq("appleandmango")

# method 3 using get()
def char_freq(string):
    new = {}
    for keys in string:
        new[keys] = new.get(keys,0)+1
    print(str(new))

# char_freq("appleandmango")

# method 4 : using count() and set()
def char_freq(string):
    string = {i:string.count(i) for i in string }
    print(str(string))

char_freq("aaabbbbccd")