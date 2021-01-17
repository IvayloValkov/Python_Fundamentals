n = int(input())

ships_army = []
ships_destroyed = 0

for i in range(n):
    ships = input().split(" ")
    ships = list(map(int, ships))
    ships_army.append(ships)

attacks = input().split(" ")

for element in attacks:
    attack = element.split("-")

    row = int(attack[0])
    column = int(attack[1])

    if ships_army[row][column] < 1:
        continue

    elif ships_army[row][column] > 1:
        ships_army[row][column] -= 1

    elif ships_army[row][column] == 1:
        ships_army[row][column] -= 1
        ships_destroyed += 1

print(ships_destroyed)