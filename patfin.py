#program to find all the numbers
import re

sentence = "This program has 10 lines and 100 characters and 200 special characters"
pattern = re.compile("\d+")
print(pattern.findall(sentence))