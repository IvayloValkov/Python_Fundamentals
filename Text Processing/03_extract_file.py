files = input().split(chr(92))

file = files[-1]

file_name = file.split(".")[0]
extension = file.split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")




