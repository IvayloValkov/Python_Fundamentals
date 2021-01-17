import re
data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, data)
numbers = [num.group() for num in numbers]
print(*numbers)