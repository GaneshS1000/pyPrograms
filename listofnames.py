#program to modify the list of names
names = ["Anil","Amol","Aditya","Avi","Alka"]
names.insert(2,"Anuj")
print(names)
names.append("Zulu")
print(names)
names.remove("Avi")
print(names)
names[0] = "AnilKumar"
print(names)
names.sort()
print(names)
newnames = sorted(names,reverse=True)
print(newnames)