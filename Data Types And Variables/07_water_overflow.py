water_tank = 255

n = int(input())
capacity = 0

for quantity in range(1, n + 1):
    liters = int(input())
    capacity += liters
    if capacity > water_tank:
        print(f'Insufficient capacity!')
        capacity -= liters
print(f'{capacity}')