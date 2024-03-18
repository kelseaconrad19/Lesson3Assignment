# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.
# Task 1: Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
good_students = []

for name in submitted:
    if name in attended:
        good_students.append(name)
    else:
        pass
print(good_students)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
if submitted is attended:
    print("identical")
else:
    print("not identical")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

for name in attended:
    if name not in submitted:
        attended.remove(name)
    else:
        pass
print(attended)
