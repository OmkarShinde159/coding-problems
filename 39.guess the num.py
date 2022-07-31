'''
Write a program able to play the "Guess the number"­game, where the number to be guessed is randomly
chosen between 1 and 20.

>>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!
'''

import random

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ran = random.choice(num)
# print(ran)

name = (input("hello ! whats your name? \n"))
# print(name)
print("well",name,"I am thinking of a number between 1 and 20")

ch = int(input("Take a guess\n"))
num1 = ran
count = 0
while ch != ran:
    if True:
        print("Your choice is too low")
        ch = int(input("Take a guess\n"))
        count += 1
else:
    count += 1
    print("Good job",name,"You guessed number in",count,"guesses" )

# # count -= 1








