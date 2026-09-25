#Use patterns from the some kind of data from the data
#re Regular Expressions library 
#re.search(patterns, string, flags =0)

import re 

email = input("What's your email?").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE()):
    print("Valid")
else:
    print("Invalid")
 
 
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
    
    