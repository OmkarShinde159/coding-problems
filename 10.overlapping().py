'''
Define a function overlapping()
that takes two lists and returns True 
if they have at least one member in common, False otherwise. 
You may use your is_member()function, or the in operator, but for the sake
of the exercise, you should (also) write it using two nested for­ loops.
'''

def overlapping(list1,list2):
    # using list slicing

    for x in (list1):
        for y in (list2):
            if x == y:
                return True
                      
    else:
        return False
            
list1 = [1,2,"c",7,"i"] 
list2 = [3,8,8,"i"]
print(overlapping(list1, list2))

