text = input()
power = 0
index = 0

while index < len(text):
    char = text[index]

    if char == ">":
        power += int(text[index+1])
    elif power > 0:
        text = text[:index] + text[index+1:]
        index -= 1
        power -= 1

    index += 1
print(text)