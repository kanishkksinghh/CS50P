class Student:
    def __init__(self, name, house): 
        if not name:
            raise ValueError("Missing Value")
        self.name = name
        self.house = house

    # This controls what prints when you print the object directly
    def __str__(self):
        return f"{self.name} from {self.house} also {self.local_area}"
    
    @property
    def house(self):
        return self.house
    
    @house.setter
    def house(self, house):
        if house not in ["Vikas", "GomtiNagar", "Lucknow"]:
            raise ValueError("Invalid House")
        self.house = house
    

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    local_area = input("Local Area: ")
    return Student(name, house, local_area)

if __name__ == "__main__":
    main()
