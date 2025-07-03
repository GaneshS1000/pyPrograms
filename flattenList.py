#program to flatten the list

numbers = [1,3,5,7,9]
numbers[2] = [2,4,6,8]
newnumbers = []
for x in numbers:
    if type(x) == list:
        for y in x:
            newnumbers.append(y)
    if type(x) !=list:
        newnumbers.append(x)
newnumbers.sort()
print(newnumbers)