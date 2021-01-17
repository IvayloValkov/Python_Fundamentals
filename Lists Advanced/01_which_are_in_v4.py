words = input().split(", ")
string = input()

result_list = [word for word in words if word in string]
print(result_list)