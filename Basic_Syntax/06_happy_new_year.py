# year = int(input())
# while True:
#     year += 1
#     current_year = year
#     first_digit = current_year // 1000
#     current_year = current_year % 1000
#     second_digit = current_year // 100
#     current_year = current_year % 100
#     third_digit = current_year // 10
#     fourth_digit = current_year % 10
#     if first_digit != second_digit and first_digit != third_digit and first_digit != fourth_digit and second_digit != third_digit and second_digit != fourth_digit and third_digit != fourth_digit:
#         print(year)
#         break

year = int(input())

while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        print(year)
        break