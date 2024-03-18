grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and print
grades.sort(reverse=True)
print(grades)
# Calculate the average grade and print
total = 0
eval_grades = []
for num in grades:
    total += num
    eval_grades.append(num) if num >= 80 else eval_grades.append("Failed")
average = total / len(grades)
print(average)
print(eval_grades)
# Replace any value below 80 with the value Failed
