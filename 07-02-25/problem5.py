# You have a list of tuples representing students and their marks:
# students = [("Ajay", 85), ("Bala", 92), ("Charan", 78), ("Deepak", 88)]
# Use a lambda function to sort the list based on marks in descending order.
# Expected Output:
# [('Bala', 92), ('Deepak', 88), ('Ajay', 85), ('Charan', 78)]

students = [("Ajay", 85), ("Bala", 92), ("Charan", 78), ("Deepak", 88)]
sorted_students = sorted(students, key=lambda student: student[1], reverse = True)  # Sorting by marks
print(sorted_students)
