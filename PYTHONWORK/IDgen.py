import random
import string


def generate_random_id():
    user_name = input("Enter Your name here: ")
    NUMBERS = string.digits
    ids = []
    for _ in range(2):  # generate 2 IDs
        DIGITS = "".join(random.choice(NUMBERS) for _ in range(2))
        user_id = user_name + DIGITS
        ids.append(user_id)
    return ids

print(generate_random_id())
