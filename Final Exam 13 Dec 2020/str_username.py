username = input()

line = input()

while not line == "Sign up":
    line = line.split(" ")

    if line[0] == "Case":
        command = line[1]
        username = eval(f"username.{command}()")
        # if case == "upper":
        #     username = username.upper()
        # else:
        #     username = username.lower()
        print(username)
    elif line[0] == "Reverse":
        startIndex = int(line[1])
        endIndex = int(line[2])
        if 0 <= startIndex <= endIndex < len(username):
            reversed_string = ''.join(reversed(username[startIndex:endIndex+1]))
            print(reversed_string)

    elif line[0] == "Cut":
        substring = line[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif line[0] == "Replace":
        char = line[1]
        username = username.replace(char, "*")
        print(username)

    elif line[0] == "Check":
        char = line[1]
        if char in username:
            print("valid")
        else:
            print(f"Your username must contain {char}.")


    line = input()