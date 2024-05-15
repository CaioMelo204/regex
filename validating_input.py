import re

def validate_username(username):
    pattern = r'^[a-zA-Z]+[\w]*$'
    
    match = re.fullmatch(pattern, username)
    return match is not None

def validate_numeric(n): 
    pattern = r'^\d+$'
    
    match = re.fullmatch(pattern, n)
    return match is not None

def validate_numeric_float(n):
    pattern = r'^-?\d+(\.\d+)?$'
    
    match = re.search(pattern, n)
    return match is not None

# user_input = input("Enter a username:   ")

numeric_input = input("Enter a numeric: ")

# if validate_username(user_input):
#     print("Valid username")
# else:
#     print("Invalid username")
    

# if validate_numeric(numeric_input):
#     print("Valid number")
# else:
#     print("Invalid number")


if validate_numeric_float(numeric_input):
    print("Valid number")
else:
    print("Invalid number")