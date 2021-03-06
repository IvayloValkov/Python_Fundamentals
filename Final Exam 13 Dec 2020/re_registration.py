import re


pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"
n = int(input())
total_count = 0
for m in range(n):
    registration = input()
    match = re.match(pattern, registration)

    if match is None:
        print("Invalid username or password")
        continue

    total_count += 1
    print("Registration was successful")
    print(f"Username: {match[1]}, Password: {match[2]}")

print(f"Successful registrations: {total_count}")