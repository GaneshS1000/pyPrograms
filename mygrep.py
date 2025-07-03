import sys
import re

pat = sys.argv[1]
inFile = sys.argv[2]

inFilePtr = open(inFile, "r")

for lineStr in inFilePtr:
    if re.search(pat, lineStr):
        print(lineStr)

inFilePtr.close()