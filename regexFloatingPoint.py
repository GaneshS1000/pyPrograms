# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
numberOfTestcases = int(input())
flag = True
for _ in range(numberOfTestcases):
    num = input()
    result = re.fullmatch(r"[+-]?[0-9]*\.[0-9]*",num)
    if result:
        print("True")
    else:
        print("False")
