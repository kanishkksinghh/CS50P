import csv

students = []

with open("students.csv") as file:
     reader = csv.reader(file)
     for name, college in reader:
         students.append({"name": name, "college": college})
    

for student in sorted(students, key=lambda student: student["name"]):
     print(f"{student['name']} is from {student['college']}")