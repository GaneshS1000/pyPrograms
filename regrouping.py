# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

inpStr = input()

m = re.search(r"([a-zA-Z0-9])\1", inpStr)

if m == None:
    print(-1)
else:
    print(m.group(0)[0])