
word = "I am an Automation Engineer"
new = word.split(" ")
text=""
for word in new:
    text = text+word
print(text.lower())
print(len(text))
charCount = dict()
for char in text.lower():
    charCount.update({char:text.count(char)})
print(charCount)