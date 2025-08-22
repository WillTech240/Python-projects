import random
import string

def generate_random_id():
    characters = string.ascii_letters + string.digits
    user_id = "".join(random.choice(characters) for _ in range(5))
    return user_id
print(generate_random_id())
