#program to count the no. of vowels in the string

print("Enter the string")
word = input()
count = 0
for x in word:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
        count = count + 1
print("No. of Vowels :",count)