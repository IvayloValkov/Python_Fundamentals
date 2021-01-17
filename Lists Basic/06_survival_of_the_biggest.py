numbers_as_string = input().split()
numbers = []
for num in numbers_as_string:
    numbers.append(int(num))
numbers_to_remove = int(input())
for n in range(numbers_to_remove):
    numbers.remove(min(numbers))
print(numbers)

# numbers_str = input().split()
# numbers = []
# for num in numbers_str:
#     numbers.append(int(num))
# remover = int(input())
# for _ in range(remover):
#     numbers.remove(min(numbers))
# print(numbers)
