# class Cat:
#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")
    
# cat = Cat()
# cat.meow

# MEOW = 3

# MEOW = 4

# for _ in range(MEOW):
#     print("Meow")
 
def meow(n: int) -> None:
    return "meow\n" * n
        
number: int = input("Number: ")
meows: str = meow(number)
print(meows, end="")
