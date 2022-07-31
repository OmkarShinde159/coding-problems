'''
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).

'''

filename = "test1.txt"
output_filename = "test2.txt"
fin = open("test1.txt","r")
fout = open("test2.txt","w")
lines = fin.readlines()
# word_dict = dict()
cnt = 0
for line in lines:
    cnt += 1
    # print(cnt)
    output_line = str(cnt) + ". "+ line
    fout.write(output_line)

print("Lines are numbered. check: "+output_filename)
fin.close()
fout.close()





    

 
