students = [
    {"name": "Kanishk", "house": "Gomti Nagar"},
    {"name": "Rohit", "house": "Gomti Nagar"},
    {"name": "Shashank", "house": "Anuskha's House"},
    {"name": "Aman", "house": "Golapur"} 
]

houses = set()
for student in students:
    if student in students:
        houses.add(student["house"])
    
for house in sorted(houses):
    print(house)