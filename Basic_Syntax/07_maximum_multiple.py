# Divisor = int(input())
# Bound = int(input())
# maximum = 0
#
# for N in range(1, Bound + 1):
#     if N % Divisor == 0:  # Числото, което търсим
#         maximum = N
#
# print(maximum)

divisor = int(input())
bound = int(input())

for num in range(bound, 0, -1):
    if num % divisor == 0:
        print(num)
        break


# divisor = int(input())
# bound = int(input())
# number = 0
# for n in range(1, bound + 1):
#     if n % divisor == 0:
#         number = n
# print(number)

# a = int(input())
# b = int(input())
# result = 0
# for n in range(a, b+1):
#     if n % a == 0 and b >= n > 0:
#         if result <= n:
#             result = n
#     else:
#         continue
# print(result)