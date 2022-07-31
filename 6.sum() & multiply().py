'''
Define a function sum()and a function multiply()
that sums and multiplies (respectively) all the
numbers in a list of numbers. 
For example, sum([1, 2, 3, 4])should return 10, 
and multiply([1, 2, 3, 4])should return 24
'''
def sum(list):
    # list = [1,2,3,4]
    add = 0
    for i in list:
        add = add + i
    print("Sum of list is : ",add)

    mul = 1
    for i in list:
        mul = mul * i
    print("Multiplication of list is: ",mul)
sum([1,2,3,4])

