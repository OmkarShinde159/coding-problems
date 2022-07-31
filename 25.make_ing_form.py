'''
In English, the present participle is formed by adding the suffix ­ing to the infinite form: go ­> going. A simple
set of heuristic rules can be given as follows:
1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
2. If the verb ends in ie, change ie to y and add ing
3. For words consisting of consonant­vowel­consonant, double the final letter before adding ing
4. By default just add ing
Your task in this exercise is to define a function make_ing_form()which given a verb in infinitive form
returns its present participle form. Test your function with words such as lie, see, move and hug. However,
you must not expect such simple rules to work for all cases.

'''
# 1. make = making, move = moving
# 2. lie = lying
# 3. hug = hugging
# 4. add = adding

def make_ing_form(word):
    word = word.lower()

    if word.endswith("ie"):
        word = word[:-2] + "ying"
        print(word)

    elif word.endswith("e"):
        word = word[:-1] + "ing"
        print(word)

    elif word[-2] in "aeiou":
        word += word[-1] + "ing"
        print(word)

    else:
        print(word+"ing")



make_ing_form("Lie")
make_ing_form("MAKE")
make_ing_form("hug")
make_ing_form("add")
