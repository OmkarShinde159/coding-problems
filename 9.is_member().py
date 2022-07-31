'''
Write a function is_member()that takes a value 
(i.e. a number, string, etc) x and a list of values a, and
returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the inoperator does,
but for the sake of the exercise you should pretend 
Python did not have this operator.
'''

# def is_member(values,list):
def is_member(x,a):
    if type(x) == str:
        x = x.split(" ")
        if x.count(a) > 0:
            return True
        else:
            return False
    else:
        if x.count(a) > 0:
            return True
        else:
            return False
  
print(is_member([1,2,3,4],5))
print(is_member("P y t h o n","O"))
print(is_member([1.1,2.1,3.1,4.1],1.1))

