'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file
name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps
to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include
the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!

'''
# paws = swap
def semordnilap(filename):
    with open(filename,'r') as f:
        words = f.read().lower().split()
        # print(words)            # returns in list form
        res = []
        for x in words:
            for y in words:
                if x == y[::-1]:
                    res.append(x+" "+x[::-1])
        print(res)
  
semordnilap("test1.txt")