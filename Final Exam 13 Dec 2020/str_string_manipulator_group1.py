string = input()

com = input()

while not com == "End":
    com = com.split(" ")
    command = com[0]

    if command == "Translate":
        char = com[1]
        replace = com[2]
        if char in string:
            string = string.replace(char, replace)
            print(string)
    elif command == "Includes":
        new_string = com[1]
        if new_string in string:
            print("True")
        else:
            print("False")
    elif command == "Start":
        start = com[1]
        print(string.startswith(start))
    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = com[1]
        print(string.rfind(char))
    elif command == "Remove":
        start = int(com[1])
        count = int(com[2])
        string = string.replace(string[start:start+count], "")
        print(string)

    com = input()