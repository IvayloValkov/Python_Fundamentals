def calculation_factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


number_1 = int(input())
number_2 = int(input())

factorial_number_1 = calculation_factorial(number_1)
factorial_number_2 = calculation_factorial(number_2)
res = factorial_number_1 / factorial_number_2
print(f"{res:.2f}")