def smallest_number(num_1, num_2, num_3):
    min_number = 9999999999
    if num_1 < min_number:
        min_number = num_1
    if num_2 < min_number:
        min_number = num_2
    if num_3 < min_number:
        min_number = num_3
    return min_number


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_number(number_1, number_2, number_3))
