'''
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and
prints the line to the screen if it is a palindrome
'''

# palindrome :  x = str[::-1]



def openFile(filename):
    with open(filename,'r') as f:
        for line in f:
            strp_line = line.strip()
            if strp_line == strp_line[::-1]:
                print(strp_line)

openFile('test.txt')        




