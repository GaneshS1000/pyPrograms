#program to check whether the string is a palindrome

print("Enter the string")
word = input()
length = len(word)
flag = True
for i in range(len(word)):
    if word[i] == word[length-i-1]:
        flag = True
    else:
        flag = False

if flag == True:
    print("Palindrome")
else:
    print("Not a Palindrome")