parking_lot = int(input())

parking = {}

for i in range(parking_lot):
    args = input().split()
    commands = args[0]
    username = args[1]

    if commands == "register":
        license_plate_number = args[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
            continue
        parking[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")

    elif commands == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
            continue
        parking.pop(username)
        print(f"{username} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")
