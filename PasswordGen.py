import random
import string

def password_generator():
    print(" Password Generator")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print(" Length must be greater than zero.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        print(f" Your generated password is: {password}")
    except ValueError:
        print(" Please enter a valid number.")

password_generator()
