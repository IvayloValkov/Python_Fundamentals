# def palindrome_number(str_num):
#     reversed_num = str_num[::-1]

#     # is_palindrome = True
#     #
#     # if str_num != reversed_num:
#     #     is_palindrome = False
#
#     # return is_palindrome
#     return True if str_num == reversed_num else False
#
#
# number_as_string = input()
# print(palindrome_number(number_as_string))

def palindrome_number(string_number):
    lenght = len(string_number)
    is_palindrome = True
    for i in range(lenght // 2):
        if string_number[i] != string_number[lenght - 1 - i]:
            is_palindrome = False
            break

    return is_palindrome


number_as_string = input().split(", ")
for num in number_as_string:
    print(palindrome_number(num))