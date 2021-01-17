lost_fights_count = int(input())
price_helmet_repair = float(input())
price_sword_repair = float(input())
price_shield_repair = float(input())
price_armor_repair = float(input())

total_repair = 0
counter_shield_repair = 0

for n_fight in range(1, lost_fights_count + 1):
    if n_fight % 2 == 0:
        total_repair += price_helmet_repair

    if n_fight % 3 == 0:
        total_repair += price_sword_repair

    if n_fight % 2 == 0 and n_fight % 3 == 0:
        total_repair += price_shield_repair
        counter_shield_repair += 1
        if counter_shield_repair % 2 == 0:
            total_repair += price_armor_repair

print(f'Gladiator expenses: {total_repair:.2f} aureus')
