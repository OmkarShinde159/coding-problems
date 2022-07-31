'''
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
ignored.
'''
import re
def palindrome_recognizer(phrase):
    phrase = phrase.lower()
    print(phrase)

    regex = "[ ]"
    phrase = (re.sub(regex,"",phrase))
    print(phrase)
   
    regex = "[^A-Za-z0-9]"
    phrase = (re.sub(regex,"",phrase))
    print(phrase)

    y = phrase[::-1]
    x = phrase[::1]
    return x == y

# phrase = ("Dammit, I'm mad!")
# print(palindrome_recognizer(phrase))

# print(palindrome_recognizer("Satan, oscillate my metallic sonatas"))

# line = ("I roamed under it as a tired  nude Maori")
# print(palindrome_recognizer(line))


def palindrome(s):
    output = [x for x in s if x!=" " and x!="," and x!= "?" and x!="!"]
    output.reverse()
    # print(output)
    str = ""
    print('Reverse string is: ',str.join(output))
    
palindrome("omkar?manish!shinde,")