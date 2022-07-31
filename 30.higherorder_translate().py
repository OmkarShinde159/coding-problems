'''
Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
"christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}and
use it to translate your Christmas cards from English into Swedish. Use the higher order function map()to
write a function translate()that takes a list of English words and returns a list of Swedish words.
'''



dict = {"merry":"god","christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def myFunc(word):
    return [dict[x] for x  in dict if word == x]

wo = ["merry","christmas","and","happy","new","year"]
res = list(map(myFunc,wo))
print(res)


def myFunc(word):
    for x in dict.keys():
        if word == x:
            return dict[x]
res = ["merry","christmas","and","happy","new","year"]

x = list(map(myFunc, res))
print(x)


