#program to validate an email address
import re
print("Enter the email")
email = input()
match = re.match(r"[a-zA-Z][a-zA-Z0-9]{0,9}@[a-zA-Z]{1,10}\.[a-z]{2,3}",email)

if match:
    print("Match Found :",match.group())
else:
    print("No Match Found")