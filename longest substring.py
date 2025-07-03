#program to find the length of the longest substring

test = "This is a Sample Programming Task"
stringlist = test.split(" ")
largest = ""
max = 0
for word in stringlist:
    if len(word)>max:
        max = len(word)
print("The Largest Substring is:",max)