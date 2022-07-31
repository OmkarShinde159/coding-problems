'''
Write a function translate()that will translate 
a text into "rövarspråket" (Swedish for "robber's
language"). 
That is, double every consonant and place an occurrence 
of "o"in between. 
For example,
translate("this is fun")
should return the string "tothohisos isos fofunon"
'''
# what is consonant ? except " a e i o u" all chars are called 
# create a variable for consonant
# create empty variable to add strings later
# access the chars in sentence using for loop
# use if else condition to insert o and double each char
# print function


def translate(sentence):
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    translate = ""
    for i in sentence:
        if i in consonant:
            translate += (i+"o"+i)
        else:
            translate += i 
    return translate
print(translate("this is fun"))






    

    
