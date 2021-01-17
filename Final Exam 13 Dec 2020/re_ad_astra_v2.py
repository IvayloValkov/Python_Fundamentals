import re

string = input()
pattern = r"(#|\|){1}(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"

total_calories = 0
matches = re.finditer(pattern, string)

for match in matches:
    total_calories += int(match['calories'])
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

matches = re.finditer(pattern, string)
for match in matches:
    print(f"Item: {match['item']}, Best before: {match['date']}, Nutrition: {match['calories']}")