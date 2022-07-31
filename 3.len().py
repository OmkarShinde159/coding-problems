'''
Define a function that computes the length of a given list
or string. (It is true that Python has the len()
function built in, 
but writing it yourself is nevertheless a good exercise.)
'''
# create a variable of string
# iterate the string chars
# count the chars
def length_of_str(str):
# str = "Python"
    count = 0
    for char in str:
        count = count + 1
    print("String length is: ",count)
length_of_str("Python123")
