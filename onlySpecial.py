#program to print only special characters

givenString = "123#$$$%abcdE"
specialchars =""
for char in givenString:
    if not char.isalnum():
        specialchars = specialchars + char
print(specialchars)
