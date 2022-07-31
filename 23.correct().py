'''
Define a simple "spelling correction" function correct()that takes a string and sees to it that 
1) two or more occurrences of the space character is compressed into one, and 
2) inserts an extra space after a period if the period is directly followed by a letter.
 E.g. correct("This   is very funny and cool.Indeed!")
should return "This is very funny and cool. Indeed!"
Tip: Use regular expressions!

'''
import re

spell = "This   is very funny and cool.Indeed!"

def correct(spell):   
    spell = re.sub(r'(?<=[.,])(?=[^\s])',r' ',spell)
    # print(spell)
    pattern  = " "+'{2,}'
    correct = re.sub(pattern," ",spell,flags = re.IGNORECASE)
    return correct

print(correct("This   is very funny and cool.Indeed!"))
print(correct("You            are so simple.Like me."))
print(correct("I    had breafast,today"))