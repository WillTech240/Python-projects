#A function is a reusable block of code or programming statements designed to perform a certain task. 
# To define a function, Python provides the def keyword.
#  The following is the syntax for defining a function. 
# The function block of code is executed only if we call it.
def generate_full_name():
    first_name = "Wilfred"
    sur_name = "Osei Bonsu"
    space = " "
    full_name = first_name + space + sur_name
    return full_name
print(generate_full_name())

def generate_full_name(first_name, sur_name):
    space = " "
    full_name = first_name + space + sur_name
    return full_name
print('FullName:',generate_full_name('Wilfred', 'Osei Bonsu'))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))

#nested function
def pow_number(a):
    return a**a
def workout(b, c):
    return b(c)
print(workout(pow_number, 2))

#area of a circle
def area_circle(r, π=22/7):
    return π * r * r
print(area_circle(7))

#Adds all numbers
def add_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total
num1 = input("Enter your numbers here: ")
num_list = [int(n) for n in num1.split()]
print(add_all(*num_list))

#Calculate slope or gradient of a line
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("Slope is undefined (vertical line).")
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1,2,3,4))

#Declare a function named print_list. It takes a list 
# as a parameter and it prints out each element of the list.
def print_list(items):
    for element in items:
        print(element)

#Write different functions which take lists. 
# They should calculate_mean, calculate_median,
#  calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
from collections import Counter
import math

# Mean
def calculate_mean(data):
    return sum(data) / len(data)

# Median
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:   # even length
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:            # odd length
        return sorted_data[mid]

# Mode
def calculate_mode(data):
    freq = Counter(data)
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    if len(modes) == len(freq):  # all values appear equally
        return None
    return modes if len(modes) > 1 else modes[0]

# Range
def calculate_range(data):
    return max(data) - min(data)

# Variance (Population variance by default)
def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Standard Deviation
def calculate_std(data):
    return math.sqrt(calculate_variance(data))

#Type of data type
def same_data_type(lst):
    if not lst:   # handle empty list
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print(same_data_type([1, 2, 3, 4]))         
print(same_data_type(["a", "b", "c"]))      
print(same_data_type([1, "two", 3]))        
print(same_data_type([]))                   
