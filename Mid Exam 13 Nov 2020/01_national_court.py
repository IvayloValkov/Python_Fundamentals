emp_1_efficiency = int(input())
emp_2_efficiency = int(input())
emp_3_efficiency = int(input())
count_people = int(input())

all_efficiency_per_hour = emp_1_efficiency + emp_2_efficiency + emp_3_efficiency
hours = 0

while count_people > 0:
    hours += 1
    count_people -= all_efficiency_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")