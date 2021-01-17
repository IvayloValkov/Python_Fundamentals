username = input()

line = input()

while not line == "Sign up":
    tokens = line.split(" ")
    command = tokens[0]

    if command == "Case":
        case = line[1]
        username = eval(f"username.{case}()")
        # if case == "upper":
        #     username = username.upper()
        # else:
        #     username = username.lower()
        print(username)
    elif command == "Reverse":
        startIndex = int(tokens[1])
        endIndex = int(tokens[2])
        if 0 <= startIndex < len(username) <= endIndex < len(username):
            reversed_string = ''.join(reversed(username[startIndex:endIndex+1]))
            print(reversed_string)

    elif command == "Cut":
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = tokens[1]
        username = username.replace(char, "*")
        print(username)

    elif command == "Check":
        char = tokens[1]
        if char in username:
            print("valid")
        else:
            print(f"Your username must contain {char}.")


    line = input()