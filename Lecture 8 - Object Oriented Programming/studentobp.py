def main():
    student = get_student()
    if student ["name"] == "Kanishk":
        student["house"] = "Vikas"
    print(f"{student['name']} from {student['house']}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house] #[name, house] list mutable(can be changed)
# #(name, house) tuple

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

def get_student():
    name= input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

    

if __name__ == "__main__":
    main()