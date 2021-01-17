import re

data = input()

pattern = r"\d+"
while True:
    if not data:
        break
    else:
        numbers = re.findall(pattern, data)
        for num in numbers:
            print(num, end=" ")

    data = input()