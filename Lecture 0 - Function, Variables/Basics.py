#ask user for their name
name =  input("What's your name?").strip().title() # input function

#remove the extra whitespace
#name = name.strip()

#it captialize the all text
#name = name.capitalize()

#it captialize all the text
#name = name.title()

#name = name.title().strip()


first, last = name.split(" ")
#Say hello to the user 
#print("Hello",name)  #print funtion
print(f"Hello, {first}")
