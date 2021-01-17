command = input()

courses = {}

while not command == "end":
    args = command.split(" : ")
    course_name = args[0]
    student_name = args[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]),reverse=True))

for key, value in sorted_courses.items():
    print(f"{key}: {len(value)}")

    for student_name in sorted(value):
        print(f"-- {student_name}")