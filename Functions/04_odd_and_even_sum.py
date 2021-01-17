def sum_of_numbers(single_number):
    even_sum = 0
    odd_sum = 0
    for ch in number:
        num = int(ch)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
result = sum_of_numbers(number)
print(result)