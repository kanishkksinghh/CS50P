def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
    
'''  
def print_square(size):
    #for each row in Sqare
    for i in range(size):
        #for each brick in row
        for j in range(size):
         print("#", end="")
    print()
''' 
main()