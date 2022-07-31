'''
Write a procedure char_freq_table()that, when run in a terminal, accepts a file name from the user,
builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
character frequency table to the screen.
'''
import re

def char_freq(filename):
    with open (filename,'r') as f:
        words = f.read().lower().replace(" ","").replace("\n","")
        # print(words)
        # print(type(words))
        dis = {key: 0 for key in words}
        for w in words:
            dis[w] += 1
        for y in dis:   
            # print("%s:%s" % (y,dis[y]))
            print(y,":",dis[y])


        
char_freq("test.txt")