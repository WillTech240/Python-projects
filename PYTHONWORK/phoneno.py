import random
import string

# store numbers
generated_numbers = set()

def phone_number_gen():
    prefix = "+233"
    characters = string.digits
    valid_prefixes = ["24", "54", "20", "50", "27", "57"]

    while True:
        start = random.choice(valid_prefixes)
        number = "".join(random.choice(characters) for _ in range(7))
        phone_number = prefix + start + number
        
        if phone_number not in generated_numbers:
            generated_numbers.add(phone_number)
            return phone_number
#print it  in my range
for _ in range(2):
    print(phone_number_gen())

print("\nTotal unique numbers stored:", len(generated_numbers))
