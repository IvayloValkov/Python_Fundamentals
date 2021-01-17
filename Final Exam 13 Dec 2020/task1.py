username = input()

line = input()

while not line == "Sign up":
    tokens = line.split()
    command = tokens[0]

    if command == "Case":
        if tokens[1] == "lower":
            username = username.lower()
            print(username)
        elif tokens[1] == "upper":
            username = username.upper()
            print(username)
    elif command == "Reverse":
        startIndex = int(tokens[1])
        endIndex = int(tokens[2])
        if 0 <= startIndex <= endIndex < len(username):
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
        new_char = tokens[1]
        if new_char in username:
            print("Valid")
        else:
            print(f"Your username must contain {new_char}.")

    line = input()