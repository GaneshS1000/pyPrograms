#program to reverse a list without using built-in function

fruits = ["apple","banana","orange","grapes"]
print("Method 1")
print(fruits[::-1])
print("Method 2")
newfruits = []
for i in range(len(fruits)):
    newfruits.append(fruits[-i])
print(newfruits)
