def get_letter_position(letter):
    num = 96
    if letter.isupper():
        num = 64

    return ord(letter) - num


lines = input().split()
total_sum = 0

for line in lines:
    first_letter = line[0]
    position_first = get_letter_position(first_letter)
    last_letter = line[-1]
    position_last = get_letter_position(last_letter)
    number = int(line[1:-1])

    current_result = 0
    if first_letter.isupper():
        current_result += number / position_first
    else:
        current_result += number * position_first

    if last_letter.isupper():
        current_result -= position_last
    else:
        current_result += position_last

    total_sum += current_result

print(f'{total_sum:.2f}')
