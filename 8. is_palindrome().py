'''
Define a function is_palindrome()
that recognizes palindromes 
(i.e. words that look the same written
backwards). 
For example, is_palindrome("radar")should return True.'''

def is_palindrome(str):
    #str = "radar"
    x = str[::-1]
    # print(x)
    y = str[::1]
    # print(y)
    return x == y
    # print(result)

print(is_palindrome("radar"))
print(is_palindrome("mango"))
print(is_palindrome("madam"))
print(is_palindrome("level"))
print(is_palindrome("civic"))





    