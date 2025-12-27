
students = {
    "Amit": 85,
    "Riya": 92,
    "Rahul": 78,
    "Neha": 88}



name = input("Enter student name: ")

if name in students:
    print("Marks:", students[name])
else:
    print("Student not found.")
