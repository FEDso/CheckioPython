import re

passw = input()

if (len(passw) < 10 or not re.match("[a-zA-Z0-p]+", passw) 
    or not re.search("[a-z]+", passw) or not re.search("[A-Z]+", passw) 
    or not re.search("[0-9]+", passw)):
    print(False)
else:
    print(True)
