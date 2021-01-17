substrings = input().split(", ")
strings = input()
#strings = input().split(", ")

result = [substring for substring in substrings if substring in strings]

#result = []

# for substring in substrings:
#     for string in strings:
#         if substring in string and substring not in result:
#             result.append(substring)

print(result)