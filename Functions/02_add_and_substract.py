# def sum_numbers(num_1, num_2):
#     result_1 = num_1 + num_2
#     return result_1
#
#
# def subtract(num_3):
#     sum_numbers(num_1=number_1, num_2=number_2)
#     result_2 = sum_numbers(num_1=number_1, num_2=number_2) - num_3
#     print(result_2)
#
#
# def add_and_subtract(num_1, num_2, num_3):
#     sum_numbers(num_1, num_2)
#     subtract(num_3)
#
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# (add_and_subtract(number_1, number_2, number_3))

def sum_numbers(a, b):
    res = a + b
    return res


def subtract(a, b):
    return a - b


def solve(a, b ,c):
    sum_nums = sum_numbers(a, b)
    result = subtract(sum_nums, c)
    return result

a = int(input())
b = int(input())
c = int(input())


print(solve(a, b, c))
