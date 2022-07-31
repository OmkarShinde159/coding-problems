'''
Implement the higher order functions map(), filter()and reduce(). (They are built­in but writing
them yourself may be a good exercise.)
'''

def imp_filter(functio,lis):
    # The filter() function in Python takes a function and a list as arguments.it returns new list
    def myFunc(check):
        print("Function created ", check)

        myFunc(check)
    
    for i in myFunc:
        print(i)

imp_filter(myFunc,list)
    

