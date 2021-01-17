n = int(input())

students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

get_average = lambda x: sum(x) / len(x)
students_average_grades = {key: get_average(value) for (key, value) in students.items() if get_average(value) >= 4.5}
# students_average_grades = {}
#
# for student, grades in students.items():
#     average_grade = sum(grades) / len(grades)

#     if average_grade < 4.5:
#         continue
#
#     students_average_grades[student] = average_grade

students_average_grades = dict(sorted(students_average_grades.items(), key=lambda x: x[1], reverse=True))

for student, average in students_average_grades.items():
    print(f"{student} -> {average:.2f}")

