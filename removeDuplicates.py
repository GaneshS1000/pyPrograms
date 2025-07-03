#program to remove duplicates from a sorted list

numbers =[1,1,2,3,4,4,5,6,7,8,9,10]
onlyOnce = []
for number in set(numbers):
    onlyOnce.append(number)
print(onlyOnce)