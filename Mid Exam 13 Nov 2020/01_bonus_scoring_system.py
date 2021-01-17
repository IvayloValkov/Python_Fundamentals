# from math import ceil
#
# students = int(input())
# lectures = int(input())
# initial_bonus = int(input())
# max_bonus = -99999999999999
# max_attendees = -9999999999999999
#
# if lectures == 0:
#     print("Max bonus: 0.")
#     print('The student has attended 0 lectures.')
# else:
#     for student in range(1, students + 1):
#         student_attendance = int(input())
#         total_bonus = student_attendance / lectures * (5 + initial_bonus)
#         if total_bonus >= max_bonus:
#             max_bonus = total_bonus
#         if student_attendance >= max_attendees:
#             max_attendees = student_attendance
#
# print(f"Max Bonus: {ceil(max_bonus)}.")
# print(f"The student has attended {max_attendees} lectures.")

import math

students = int(input())
lectures = int(input())
initial_bonus = int(input())
attendance_list = []

if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(1, students + 1):
        attendances = int(input())
        attendance_list.append(attendances)

    print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
    print(f'The student has attended {max(attendance_list)} lectures.')
