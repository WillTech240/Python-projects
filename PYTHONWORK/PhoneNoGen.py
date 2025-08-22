import random
import string

def phone_number_gen():
    prefix = "+233"  
    characters = string.digits
    valid_prefixes = ["24", "54", "20", "50", "27", "57"]

    start = random.choice(valid_prefixes)  
    number = "".join(random.choice(characters) for _ in range(7))  
    
    return prefix + start + number

for _ in range(2):
    print(phone_number_gen())

