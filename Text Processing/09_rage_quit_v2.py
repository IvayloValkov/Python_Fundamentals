line = input().upper()
unique_symbol = set()
return_string = ''
text = ''

for i in range(len(line)):
    c = line[i]
    if not c.isdigit():
        text += c
    elif c.isdigit():
        dig = ''
        while i < len(line) and line[i].isdigit():
            dig += line[i]
            i += 1
        return_string += text * int(dig)
        text = ''

print(f'Unique symbols used: {len(set(return_string))}')
print(return_string)