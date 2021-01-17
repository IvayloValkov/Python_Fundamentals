budget = int(input())
money_needed = 0
months = int(input())

for month in range(1, months + 1):
    if month % 2 == 1 and not month == 1:
        money_needed -= money_needed * 0.16

    if month % 4 == 0:
        money_needed += money_needed * 0.25

    money_needed += budget * 0.25
result = abs(money_needed-budget)
if money_needed >= budget:
    print(f"Bravo! You can go to Disneyland and you will have {result:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {result:.2f}lv. more.")
