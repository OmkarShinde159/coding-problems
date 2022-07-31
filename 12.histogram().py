'''
Define a procedure histogram()that takes a list of integers and prints a histogram to the screen. For
example, histogram([4, 9, 7])should print the following:
****
*********
*******
'''

def histogram(list_of_int):
    n = len(list_of_int)
    
    for i in list_of_int[0:n]:
        print(i*"*")
        
list_of_int = ([2,3,2])
histogram(list_of_int)