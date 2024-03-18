students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1: Filter out students who have grades below 80. Print the name, grade and activity. Expected Outcome "Jane", 78, "Art"
students_approved = []
failing_students = []
for i in range(len(students)):
    stu_name = students[i]
    grade = grades[i]
    activity = activities[i]
    if grade < 80:
        failing_students = [stu_name, grade, activity]
    # Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
    else:
        students_approved.append(stu_name)

print(failing_students)
# Task 3: Print the list students_approved
print(students_approved)


