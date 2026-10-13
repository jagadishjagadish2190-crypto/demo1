# marks_calculator.py

# Accept student name and marks
student_name = input("Enter the student's name: ")
marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

# Calculate total, average and percentage
total = marks1 + marks2 + marks3
average = total / 3
percentage = (total / 300) * 100  # Assuming each subject is out of 100

# Define passing criteria
passing_marks = 35  # minimum marks to pass in each subject

# Determine pass or fail status
if marks1 >= passing_marks and marks2 >= passing_marks and marks3 >= passing_marks:
    status = "Pass"
else:
    status = "Fail"

# Display the results
print(f"\nStudent Name: {student_name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {status}")
