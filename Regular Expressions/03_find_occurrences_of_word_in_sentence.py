import re

data = input()
word = input()

pattern = rf"\b{word}\b"
words = re.findall(pattern, data, re.IGNORECASE)
print(len(words))