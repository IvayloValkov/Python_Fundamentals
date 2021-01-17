user_names = input().split(", ")


for user_name in user_names:
    if not (3 <= len(user_name) <= 16):
        continue

    is_valid = True

    for char in user_name:
        if not (char.isalnum() or char == "-" or char == "_"):
            is_valid = False
            break

    if not is_valid:
        continue

    print(user_name)
