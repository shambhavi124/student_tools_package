from student_tools import total_marks, average_marks, assign_grade, display_details

# Input details
student_name = "Sindhu"
course_name = "BCA"
marks = [85, 90, 78, 88, 92]

# Display student info
display_details(student_name, course_name)

# Calculate results
total = total_marks(marks)
average = average_marks(marks)
grade = assign_grade(average)

# Display results
print("\n--- Student Report ---")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
