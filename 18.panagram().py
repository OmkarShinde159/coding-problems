'''
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The
quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
is a pangram or not.
'''
def panagram(sentence):

# sentence = "The quick brown fox jumps over the lazy dog."
    sentence = sentence.lower()
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in sentence:
        for y in chars:
            if y not in sentence:
                return False
            else:
                return True

# sentence = "The quick brown fox  over the dog."
# print(panagram(sentence))

def isPanagram(sentence):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new = [x for x in chars if x not in sentence] 
    if new == []:return True
    else:return False

sentence = "The quick brown fox jumps over the lazy dog"
print(isPanagram(sentence))

sentence = "The quick brown fox jumps over the dog"
print(isPanagram(sentence))