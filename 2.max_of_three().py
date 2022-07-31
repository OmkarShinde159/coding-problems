'''
Define a function max_of_three()that 
takes three numbers as arguments and returns the largest of
them.
'''
# 1. create function and assign three arguments
# 2. use if else conditional 
# 3. print result

def max_of_three(a,b,c):
    if a > (b and c): 
        print(f"{a} is greater than {b} & {c}")
    elif b > (a and c): 
        print(f"{b} is greater than {a} & {c}")
    elif c > (a and b): 
        print(f"{c} is greater than {a} & {b}")
    else: 
        print("all numbers are equal")

max_of_three(10,9,8)
max_of_three(11,12,11)
max_of_three(11,2,21)
max_of_three(2,2,2)
max_of_three(10,8,10)

def max_of_three(a,b,c):
    if a > b:
        if a > c:
            print("A is greatest")
        else:
            print("C is greatest")
    else:
        if b > c:
            print("B is greatest")
max_of_three(10,8,10)

def max_of_three(a,b,c):
    if a > b and a > c:
        print("A is largest")
    elif b > a and b > c:
        print("B is largest")
    else:
        print("C is largest")
        
max_of_three(2,2,4)



    
    







