# names = []

# for _ in range(3):
#     names.append(input("What's your name?"))
    
# for name in sorted(names):
#     print(f"Hello, {name}")

#open
# name = input("What's your name?")

# with open("name.txt", "w") as file:
#     file.write(f"{name}\n")
#     file.close() 
    
with open("name.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())


for name in sorted(names, reverse=True):
    print(f"Hello, {name}")