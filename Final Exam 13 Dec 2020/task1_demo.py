string = input()

data = input()
while not data == "Done":
    command = data.split()[0]
    if command == "Change":
        char = data.split()[1]
        replacement = data.split()[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        new_string = data.split()[1]
        if new_string in string:
            print("True")
        else:
            print("False")
    elif command == "End":
        new_end = data.split()[1]
        if string.endswith(new_end):
            print("True")
        else:
            print("False")
    elif command == "Uppercase":
        string = string.upper()
        print(string)
    elif command == "FindIndex":
        char = data.split()[1]
        print(string.find(char))
    elif command == "Cut":
        start = int(data.split()[1])
        length = int(data.split()[2])
        print(string[start:start+length])

    data = input()