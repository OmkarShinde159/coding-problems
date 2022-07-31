'''
35. The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the
English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and
numbers) can be pronounced and understood by those who transmit and receive voice messages by radio
or telephone regardless of their native language, especially when the safety of navigation or persons is
essential. Here is a Python dictionary covering one version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
'f':'foxtrot',
'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo',
'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo',
's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Your task in this exercise is to write a procedure speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have
access to the system TTS (Text­To­Speech) as follows: os.system('say ' + msg), where msgis the
string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to
be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of
the pause between each spoken ICAO word, and a float indicating the length of the pause between each
word spoken.

'''
import time, os
from string import punctuation

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
'f':'foxtrot',
'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo',
'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo',
's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
'x':'x-ray', 'y':'yankee', 'z':'zulu'}

def icao(txt,icao_pause=1,word_icao=3):
    # take each word from provided string
    # convert txt into list using split() ['Hello', 'world,', 'hi,', "I'm", 'Nick!']
    words = txt.split()
    # print(words) 
    for word in words:  # acess each word in words list
        for char in word: # access each char in word 'hello' >> h e l l o
            if char not in punctuation: # ',!
                os.system('say' + d[char.lower()]) # TTS (Text-To-Speech) access
                time.sleep(icao_pause) # added wait time after every letter
        time.sleep(word_icao) # added wait time after every word


icao("Hello world, hi, I'm Nick!", 0.10, 1)
icao("The quick brown Fox jumps over the laZy Dog!")