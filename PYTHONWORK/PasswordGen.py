import random
import string

def password_generator():
    print("Password Generator")
    try:
        while True:
            length = int(input("Enter password length (5 - 12): "))

            if length < 5:
                print("Length must be at least 5.")
                continue
            elif length > 12:
                print("Length must not be greater than 12.")
                continue

            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for _ in range(length))

            print(f"Your generated password is: {password}\n")

            # Ask if user wants another password
            again = input("Do you want to generate another password? (yes/no): ").lower()
            if again != "yes":
                print("Thank you for using the password generator app")
                break

    except ValueError:
        print("Please enter a valid number.")

password_generator()
