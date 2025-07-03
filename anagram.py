#program to check if 2 strings are anagram


word1 = "listen"
word2 = "silent"
flag = True
char1 = list(word1)
char2 = list(word2)
char1.sort()
char2.sort()
if char1 == char2:
    flag = True
else:
    flag = False

if flag == True:
    print("Anagram")
else:
    print("Not an Anagram")