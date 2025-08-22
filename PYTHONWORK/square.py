import math as m

print("\nCHOOSE YOUR OPTION")
print("1. Square Root")
print("2. Exponent")
print("3. Sin")
print("4. Cos")
print("5. Tan")

choice = input("Enter your choice: ")


if choice == "1":
    def square_number():
        number = float(input("Enter your number: "))
        result = m.sqrt(number)
        print(f"Square Root of {number} is {result}")
    square_number()

elif choice == "2":
    def exponential_number():
        number = float(input("Enter your number: "))
        power = float(input("Enter the exponent: "))
        result = m.pow(number, power)
        print(f"{number} raised to the power {power} is {result}")
    exponential_number()

elif choice == "3":
    def sin_number():
        angle = float(input("Enter the angle in degrees: "))
        radian = m.radians(angle)  # convert to radians
        result = m.sin(radian)
        print(f"sin({angle}°) = {result}")
    sin_number()

elif choice == "4":
    def cos_number():
        angle = float(input("Enter the angle in degrees: "))
        radian = m.radians(angle)
        result = m.cos(radian)
        print(f"cos({angle}°) = {result}")
    cos_number()

elif choice == "5":
    def tan_number():
        angle = float(input("Enter the angle in degrees: "))
        radian = m.radians(angle)
        result = m.tan(radian)
        print(f"tan({angle}°) = {result}")
    tan_number()

else:
    print("Invalid option, Try again")
