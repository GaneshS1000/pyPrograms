#program to capitalize a sentence

allWords = "visit ykanetkar.com for online course in programming"
wordlist = allWords.split(" ")
print(wordlist)
newSentence = ""
for word in wordlist:
    newSentence = newSentence +" "+ word.capitalize()
print(newSentence)