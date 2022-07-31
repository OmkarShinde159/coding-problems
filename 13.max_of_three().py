'''
The function max()from exercise 1) and the function max_of_three()from exercise 2) will only work for
two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose
we cannot tell in advance how many they are? Write a function max_in_list()that takes a list of
numbers and returns the largest one.
'''

def max_in_list(list):
    # initialize a max element
    n = len(list)
    max = list[0]
    print(max)
    for i in range(1,n):
        # print(i)
        if list[i] > max:
            max = list[i]
    return max
            

list = [1,2,3,4,5,6,7,8,9,1,55,4,8,6,78,0]
print(max_in_list(list))

