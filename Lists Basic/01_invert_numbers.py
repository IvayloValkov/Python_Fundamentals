numbers_string = input()

numbers = numbers_string.split(" ")
inverted_numbers = []

for item in numbers:
    new_number = -(int(item))
    inverted_numbers.append(new_number)

print(inverted_numbers)