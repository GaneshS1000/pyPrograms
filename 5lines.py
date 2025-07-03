#program to read lines from a file

file1 = open("C:\\Users\\Ganesh S\\PycharmProjects\\Testing\\csvfiles\\participantnew.csv","r")
data = file1.readlines()
lines = []
count = 0
for x in data:
    if count>3:
        break
    else:
        lines.append(x)
    count = count + 1
print(lines)