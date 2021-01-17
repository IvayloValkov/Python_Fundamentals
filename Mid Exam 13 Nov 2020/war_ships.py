pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health = int(input())
command = input()
flag = 0


class Ship:
    def __init__(self, ship, max_health):
        self.ship = ship
        self.max_health = max_health

    def fire(self, index, points):
        if 0 <= index < len(self.ship):
            self.ship[index] -= points
            if self.ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                return 1
        return 0

    def defend(self, index_1, index_2, points):
        if 0 <= index_1 and index_2 < len(self.ship):
            for i in range(index_1, index_2 + 1):
                self.ship[i] -= points
                if self.ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    return 1
        return 0

    def repair(self, index, points):
        if 0 <= index < len(self.ship):
            self.ship[index] += points
            if self.ship[index] > self.max_health:
                self.ship[index] = self.max_health

    def status(self):
        need_repair = [el for el in self.ship if el < 0.2 * self.max_health]
        return need_repair

    def sum_ship(self):
        return sum(self.ship)


pi_ship = Ship(pirate_ship, maximum_health)
wa_ship = Ship(war_ship, maximum_health)

while command != "Retire":
    command = command.split()
    if command[0] == "Fire":
        flag = wa_ship.fire(int(command[1]), int(command[2]))
        if flag == 1:
            break
    elif command[0] == "Defend":
        flag = pi_ship.defend(int(command[1]), int(command[2]), int(command[3]))
        if flag == 1:
            break
    elif command[0] == "Repair":
        pi_ship.repair(int(command[1]), int(command[2]))
    elif command[0] == "Status":
        print(f"{len(pi_ship.status())} sections need repair.")
    command = input()

if flag == 0:
    print(f"Pirate ship status: {pi_ship.sum_ship()}")
    print(f"Warship status: {wa_ship.sum_ship()}")