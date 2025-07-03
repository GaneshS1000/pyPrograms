#program to perform regular expression search
import re

string = "Chatgpt"
print(re.search("[a-z|A-Z]",string))

string = "mumbai"
print(re.search("bai$",string))

email = "jacob@gmail.com"
print(re.search("\w*@gmail.com",email))

city = "Bangalore"
print(re.search("^[A-Z]",city))