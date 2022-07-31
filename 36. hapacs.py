'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written
record of a language, the works of an author, or in a single text. Define a function that given the file name of
a text will return all its hapaxes. Make sure your program ignores capitalization.
'''
def hapaxes(filename):
    with open (filename,"r") as f:
        words = f.read().lower().split()
        # print(words)
        hap = []
        for w in words:
            if words.count(w) < 2:
                hap.append(w)

        print("hapaxes are :" , hap)
        
hapaxes("hapex.txt")
   
    # regex = (r'^(?=[a-z])[a-z]$')
    # match = re.compile(regex,str(words))
    # print(match)



   