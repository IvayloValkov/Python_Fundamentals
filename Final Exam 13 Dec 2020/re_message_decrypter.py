import re

col = int(input())

pattern = r"(^\$[A-Z]{1}[a-z]{2,}\$:[ ](\[[0-9]+\]\|){3}$)|(^\%[A-Z]{1}[a-z]{2,}\%:[ ](\[[0-9]+\]\|){3}$)"

for i in range(col):
    a = input()
    match = re.findall(pattern, a)
    if match:
        a = a.split(": ")
        word = a[0]
        word = word[1:-1]

        asc = a[1].split("|")
        asc.pop()
        y = ""
        for x in asc:
            x = int(x[1:-1])
            y += chr(x)

        print(f"{word}: {y}")
    else:
        print("Valid message not found!")