#program to increment a number by 1 and convert them into a list
numbers = [1,2,3]
num = ""
for x in numbers:
    num = num + str(x)
increment = int(num) + 1
numbers = []
for x in str(increment):
    numbers.append(int(x))
print(numbers)