'''
 Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
"christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}and
use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
that takes a list of English words and returns a list of Swedish words
'''
# consider dict as python dictionary
# we search single word or list of words from dictionary
# thats why we are not convert list into string and also takes input as list
# you must understand the question and compare it with real world example

dict = {"merry":"god","christmas":"jul","and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(list):
    translate = []
    for x in list: 
        translate.append(dict[x])
    print("Swedish translation is: ",translate)

list = ["happy","new","year"]
translate(list)

