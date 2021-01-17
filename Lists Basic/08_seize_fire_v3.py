strings = input().split("#")
water = int(input())

cells = []
total_fire = 0
effort = 0
for element in strings:
    element_str = element.split()
    word = element_str[0]
    level = int(element_str[2])
    is_valid = False

    if water < level:
        continue

    if word == "High" and 81 <= level <= 125:
        is_valid = True
    elif word == "Medium" and 51 <= level <= 80:
        is_valid = True
    elif word == "Low" and 1 <= level <= 50:
        is_valid = True

    if is_valid:
        cells.append(level)
        water -= level
        effort += level * 0.25
        total_fire += level
print("Cells:")
for cell in cells:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")