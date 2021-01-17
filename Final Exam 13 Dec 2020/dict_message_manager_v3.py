capacity = int(input())

command = input()
users = {}
while not command == "Statistics":
    commands_list = command.split("=")
    current_command = commands_list[0]

    if current_command == "Add":
        name = commands_list[1]
        sent = int(commands_list[2])
        received = int(commands_list[3])
        if name not in users:
            users[name] = [sent, received]

    elif current_command == "Message":
        sender = commands_list[1]
        receiver = commands_list[2]

        if sender in users and receiver in users:
            users[sender][0] += 1

            if users[sender][0] + users[sender][1] == capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]

            users[receiver][1] += 1
            if users[receiver][0] + users[receiver][1] == capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif current_command == "Empty":
        name = commands_list[1]

        if name == "All":
            users.clear()
        else:
            del users[name]

    command = input()

print(f"Users count: {len(users)}")

sorted_list = sorted(users.items(), key=lambda x: (-x[1][1], x[0]))

for user in sorted_list:
    print(f"{user[0]} - {user[1][0] + user[1][1]}")
