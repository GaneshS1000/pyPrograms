#program to remove duplicate numbers from the list
numbers =[1,1,2,3,4,4,5,6,7,8,9,10]
onlyOnce = []
for number in numbers:
    if numbers.count(number) == 1:
        onlyOnce.append(number)
print(onlyOnce)
