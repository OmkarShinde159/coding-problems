'''
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
lengths of the word tokens in the text, divided by the number of word tokens).

'''

fn = open("test1.txt","r")
fn = fn.read().split()
wo = [len(x) for x in fn]
avg = sum(wo) / len(wo)
print("avg len of word is: ",int(avg))