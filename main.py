import random
import string

dec = True

minimum_val = 12
maximum_val = 60

def generate_password(length : int):
    
    list_of_units = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choices(list_of_units, k = length))
    
    return password

while dec:
    
    password_length = int(input("How long do you want your password to be (enter a number) : "))
    
    if password_length >= minimum_val and password_length <= maximum_val:
        
        result = generate_password(password_length)
        
        print(result)
        
        dec = False
        break
    
    else:
        
        print(f"Password length must be between {minimum_val} and {maximum_val}.")
    
    
    

