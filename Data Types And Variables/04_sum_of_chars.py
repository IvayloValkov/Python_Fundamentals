lines = int(input())
total_sum = 0
for char in range(1, lines + 1):
    letter = input()
    total_sum += ord(letter)
print(f'The sum equals: {total_sum}')