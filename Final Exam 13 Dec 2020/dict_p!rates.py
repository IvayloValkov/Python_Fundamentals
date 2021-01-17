cities = {}

data = input()
while not data == 'Sail':
    city = data.split("||")[0]
    population = data.split("||")[1]
    gold = data.split("||")[2]
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    data = input()

command = input()
while not command == 'End':

    splited = command.split("=>")
    command_type = splited[0]
    city = splited[1]
    if command_type == 'Plunder':
        people = int(splited[2])
        gold = int(splited[3])
        cities[city]["gold"] -= gold
        cities[city]["population"] -= people
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]["gold"] == 0 or cities[city]["population"] == 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif command_type == 'Prosper':
        gold = int(splited[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    command = input()


if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    sorted_cities = dict(sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0])))
    for city, peoples in sorted_cities.items():
        people = peoples['population']
        gold = peoples['gold']
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")