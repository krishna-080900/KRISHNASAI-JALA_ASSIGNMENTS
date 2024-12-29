#6.6 Matching a String Against a Regular Expression With matches()

import re

pattern = r"Python"
string = "Python is awesome!"

# Match at the beginning of the string
match = re.match(pattern, string)

if match:
    print("Match found!")
else:
    print("No match found.")
