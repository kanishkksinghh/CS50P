name = input("What's your name? ")

'''
if name =="Harry" or name=="Herminoe" or name=="Ron":
    print("Gryffindor")


        
elif name =="Draco":
    print("Slytherin")
    
else:
    print("Who")
'''

match name:
    case "Harry" |"Herminoe"| "Ron":
        print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _:
        print("Who?")
        