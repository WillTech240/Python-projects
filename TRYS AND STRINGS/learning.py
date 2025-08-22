
# 1. Whole module
import math
print("Whole module:")
print("math.sqrt(16) =", math.sqrt(16))
print()

# 2. Specific function
from math import factorial
print("Specific function:")
print("factorial(5) =", factorial(5))
print()

# 3. Alias
import random as rnd
print("Alias:")
print("Random number between 1 and 10:", rnd.randint(1, 10))
print()

# 4. All functions (use carefully!)
from math import *
print("All functions:")
print("cos(0) =", cos(0))
print("sin(45° in radians) =", sin(radians(45)))
print()

# 5. Nested import inside a function
def roll_dice():
    import random  # only loads when this function is called
    return random.randint(1, 6)

print("Nested import:")
print("Dice roll:", roll_dice())

#import module_name
#Example
import math as m
print(m.sqrt(49))
print(m.pow(7, 2))

# combining random and string
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(8))
print(password)

#Random number
import random

rand_num = random.randint(1, 10)  # picks a number from 1 to 10
print("Random number:", rand_num)

#Creating Random Password
import random
import string

characters = string.ascii_letters + string.digits
password = "".join(random.choice(characters) for _ in range(8))
print("Random password:", password)

#Import everything from a module
from math import *

#ROLL A DICE 10 TIMES
def roll_dice():
    import random
    return random.randint(1,6)

print(roll_dice())

