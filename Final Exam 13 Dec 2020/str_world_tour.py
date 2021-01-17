stops = input()

while True:
    data = input()

    if data == "Travel":
        break
    split_data = data.split(":")
    command = split_data[0]

    if command == "Add Stop":
        index = int(split_data[1])
        string = split_data[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif command == "Remove Stop":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + "" + stops[end_index + 1:]

    elif command == "Switch":
        old_string = split_data[1]
        new_string = split_data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")