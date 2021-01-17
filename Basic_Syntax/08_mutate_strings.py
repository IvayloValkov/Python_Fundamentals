# text_1 = input()
# text_2 = input()
# lenght = len(text_2)
# lenght_1 = len(text_1)
# result = ""
# result_1 = ""
# for i in range(0, lenght):
#     result_1 += text_2[i]
#     result = ""
#     for n in range(0, lenght_1):
#         if n <= i:
#             continue
#         result += text_1[n]
#     if not text_1[i] == text_2[i]:
#         print(result_1 + result)

string_1 = input()
string_2 = input()

current_string = ''
previous_string = string_1

for iteration in range(len(string_1)):
    for index_str_2 in range(0, iteration + 1):
        current_string += string_2[index_str_2]
    for index_str_1 in range(iteration + 1, len(string_1)):
        current_string += string_1[index_str_1]
    if not previous_string == current_string:
        print(current_string)
    previous_string = current_string
    current_string = ''
