import functools
import copy
'''
Define a function max()that takes two numbers as arguments 
and returns the largest of them. 
Use the if-then-else construct available in Python. 
(It is true that Python has the max()function built in, but writing it
yourself is nevertheless a good exercise.)
'''
# assign 2 numbers as an argument
# use condition to check the largest of them
# print result
def max(a,b):
    if a > b:
        print(a,"is greater than",b)
    else:
        if a == b:
            print("both numbers are equal")
        else:
            print(a,"is less than",b)

#input =  "Akshay Bhau Gholap"
#output = "yahskA uahB palohG"

def rev(string):
    x = string
    y = x.split()
    st = []
    print(y)
    for w in y:
        z = w[::-1]
        print(z)
        st.append(z)    
    print(st)
    return " ".join(st)
     
# map , reduce, filter

x = [1,2,4]
y = ['Akshay','Bhau','Gholap']


def maxi(**argv):
    for i,j in argv.items():
        print(i,j)
    # x = functools.reduce(lambda x,y: x if x>y else y, argv)
    # print(x)


x = [[1,2,3],[4,5,6],[7,8,9]]
y = copy.deepcopy(x)
print(x)
print(y)

y[0][2] = 10

print(x)
print(y)

#pass by value
# x = 8

# def eny(x):
#     print(x)  #=8 
#     x = 2
#     print(x)  #=2

# eny(x)
# print(x)     #=8

# pass reference
x = [1,2,3]

def eny(x):
    print(x)
    x[2] = 2
    print(x)

eny(x)
print(x)




