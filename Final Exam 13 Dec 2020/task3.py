# text_input = input()
# users = {}
# while not text_input == "Statistics":
#     tokens = text_input.split("->")
#     command = tokens[0]
#     username = tokens[1]
#
#     if command == "Add":
#         if username in users:
#             print(f"{username} is already registered")
#         else:
#             users[username] = []
#
#     elif command == "Send":
#         email = tokens[2]
#         users[username].append(email)
#
#     elif command == "Delete":
#         if username not in users:
#             print(f"{username} not found!")
#         else:
#             users.pop(username)
#
#     text_input = input()
#
# users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
#
# print(f"Users count: {len(users)}")
# for user, emails in users.items():
#     print(user)
#
#     for email in emails:
#         print(f" - {email}")


# print(bool(0))
# print(bool(None))
# print(bool(""))
# print(bool(-1))

def printText(text):
    print("I love" + text)
printText("Python")