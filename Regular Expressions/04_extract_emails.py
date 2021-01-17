import re

data = input()

user_pattern = r"( |^)[a-z0-9]+([\.\-_][a-z0-9]+)*"
host_pattern = r"[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"
pattern = rf"{user_pattern}@{host_pattern}"

matches = re.finditer(pattern, data)

for match in matches:
    email = match[0].strip()
    print(email)

#(^|(?<=\s))([a-zA-Z0-9])+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+($|(?=\s))