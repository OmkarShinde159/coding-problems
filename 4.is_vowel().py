'''
Write a function that takes a character
 (i.e. a string of length 1) and returns True 
 if it is a vowel, 
 False
otherwis
'''
# vowel is : a e i o u A E I O U

def is_vowel(char):
    str = char in "aeiouAEIOU"
    print(char,"Is Vovel ?: ",str)
is_vowel("Z")
is_vowel("e")
is_vowel("E")


