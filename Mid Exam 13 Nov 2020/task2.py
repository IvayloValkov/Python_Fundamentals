particles = input().split("|")

command = input()

while not command == "Done":
    command_type = command.split()[0]
    direction = command.split()[1]

    if command_type == "Move":
        if direction == "Left":
            index = int(command.split()[2])
            move = index - 1
            if index in range(len(particles)) and move in range(len(particles)):
                particles[index], particles[move] = particles[move], particles[index]
        elif direction == "Right":
            index = int(command.split()[2])
            move = index + 1
            if index in range(len(particles)) and move in range(len(particles)):
                particles[index], particles[move] = particles[move], particles[index]
    elif command.split()[0] == "Check":
        if direction == "Even":
            even_elements = [particles[i] for i in range(len(particles)) if i % 2 == 0]
            print(" ".join(map(str, even_elements)))
        elif direction == "Odd":
            odd_elements = [particles[i] for i in range(len(particles)) if i % 2 != 0]
            print(" ".join(map(str, odd_elements)))

    command = input()
weapon_name = ("".join(particles))
print(f"You crafted {weapon_name}!")