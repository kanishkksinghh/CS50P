# while True:
#     n = int(input("What's n?"))
#     if n>0:
#         break
    
# for _ in range(n):
#     print("Meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
        return n

    meow(3)
    
def meow(n):
    for _ in range (n):
        print("Meow")