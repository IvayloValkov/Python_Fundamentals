# digit = []
# letters = []
# others = []
#
# line = input()
#
# for char in line:
#     if char.isalpha():
#         letters.append(char)
#     elif char.isdigit():
#         digit.append(char)
#     else:
#         others.append(char)
#
# print(''.join(digit))
# print(''.join(letters))
# print(''.join(others))


digit = ""
letters = ""
others = ""

line = input()

for char in line:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digit += char
    else:
        others += char

print(digit)
print(letters)
print(others)