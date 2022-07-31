'''
Using the higher order function filter(), define a function filter_long_words()that takes a list of
words and an integer n and returns the list of words that are longer than n.

'''

def filter_long_words(LoW,n):
    def myFunc(x):
        if len(x) <= n:
            return False
        else:
            return True
            
    newLoW = filter(myFunc,LoW)
    # for x in newLoW:
    #     result.append(x)
    result = [x for x in newLoW]
    print(result)

LoW = ['ora','toma','swift','package']
n = 4

filter_long_words(LoW,n)


def filter_long_words(LoW,n):
    res = list(filter(lambda x: len(x) > n,LoW))
    print(res)

ro = ['om','saii','shraddha','django']   
filter_long_words(ro,2)
