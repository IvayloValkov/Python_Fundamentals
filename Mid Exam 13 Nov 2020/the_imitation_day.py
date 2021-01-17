message = input()
message_list = "".join(message)
command = input().split("|")

while not command[0] == "Decode":
    if command[0] == "Insert":
        message_list = message_list[:int(command[1])] + command[2] + message_list[int(command[1]):]

    elif command[0] == "Move":
        message_list = message_list[int(command[1]):] + message_list[:int(command[1])]

    elif command[0] == "ChangeAll":
        message_list = message_list.replace(command[1], command[2])

    command = input().split("|")

print(f"The decrypted message is: {message_list}")