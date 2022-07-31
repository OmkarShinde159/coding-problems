'''
The third person singular verb form in English is distinguished by the suffix ­s, which is added to the stem of
the infinitive form: run ­> runs. A simple set of rules can be given as follows:
1. If the verb ends in y, remove it and add ies
2. If the verb ends in o, ch, s, sh, x or z, add es
3. By default just add s

Your task in this exercise is to define a function make_3sg_form()which given a verb in infinitive form
returns its third person singular form. Test your function with words like try, brush, run and fix. Note however
that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all
cases. Tip: Check out the string method endswith().
'''

# 1. any = anies
# 2. mango = mangoes, match = matches, guess = guesses, dish = dishes, fox = foxes, roz = rozes
# 3. else : add s
import string
def infinite(word):

    if word.endswith('y'):
        word = word[:-1] + "ies"
        return word
    
    elif word.endswith('o') or word.endswith('ch') or word.endswith('s') or word.endswith('sh') or word.endswith('x') or word.endswith('z'):
        word = word + "es"
        return word

    else:
        word = word + "s"
        return word


print(infinite("any"))
print(infinite("mango"))
print(infinite("match"))
print(infinite("guess"))
print(infinite("dish"))
print(infinite("fox"))
print(infinite("roz"))
print(infinite("how"))
# print(infinite("Manish"))
