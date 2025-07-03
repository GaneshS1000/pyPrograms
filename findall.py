#program to use findall function

import re

text = "This is a sample set of sentences divided in 10 pieces which was a 100 whole"
pattern = "\d+"
match = re.findall(pattern,text)
print(match)