numbers_as_strings = input().split(" ")

sorted_numbers = sorted(numbers_as_strings, reverse=True)
print((''.join(sorted_numbers)))