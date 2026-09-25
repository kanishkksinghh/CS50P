# with open("students.csv") as file:
#     for line in file:
#         name, college = line.rstrip().split(",")  
#         print(f"{name} is in {college}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, college = line.rstrip().split(",")  
#         student = {}
#         student["name"] = name
#         student["college"] = college
#         students.append(student)
        
# for student in students:
#     print(f"{student['name']} is in {student['college']}")

students = []

with open("students.csv") as file:
     for line in file:
        name, college = line.rstrip().split(",")  
        student = {"name": name, "college": college}
        students.append(student)
        
def get_name(student):
    return student["name"]
    

for student in sorted(students, key=lambda student: student["name"]):
     print(f"{student['name']} is from {student['college']}")
