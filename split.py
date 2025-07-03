#program to split the string

import re

sentence = "This is    a sample,text,  with  @different set of characters"
print(re.split("[,\t@ ]+",sentence))