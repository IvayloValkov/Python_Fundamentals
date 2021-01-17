houses = [int(n) for n in input().split("@")]
position = 0
command = ""
while True:
    command = input().split()
    if command[0] == "Love!":
        break

    jump = int(command[1])
    position += jump

    if position > len(houses) - 1:
        position = 0
    if houses[position] <= 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] <= 0:
            print(f"Place {position} has Valentine's day.")

print(f"Cupid's last position was {position}.")

leftover = [x for x in houses if x > 0]

if len(leftover) >= 1:
    print(f"Cupid has failed {len(leftover)} places.")
else:
    print("Mission was successful.")