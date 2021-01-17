import math

biscuits = int(input())
workers = int(input())
biscuits_competition = int(input())
biscuits_per_day = 0

for day in range(1, 31):

    if day % 3 == 0:
        biscuits_per_day += int((biscuits * workers) * 0.75)
    else:
        biscuits_per_day += int(biscuits * workers)

print(f"You have produced {math.floor(biscuits_per_day)} biscuits for the past month.")

percentage = abs((biscuits_per_day - biscuits_competition) / biscuits_competition) *100
if biscuits_per_day > biscuits_competition:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")