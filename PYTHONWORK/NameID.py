import random
import string

def generate_random_id():
    user_name = input("Enter Your name here: ")
    NUMBERS =  string.digits
    characters = user_name 
    DIGITT = "".join(random.choice(NUMBERS) for _ in range(2))
    user_id = characters + DIGITT
    return user_id
print(generate_random_id())
