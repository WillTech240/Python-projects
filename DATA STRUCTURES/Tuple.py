# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (last element)

# Length of tuple
print(len(fruits))  # 3

#Tuple with Different Data Types
person = ("John", 25, 5.9, True)
print(person)

#Nested Tuple (tuple inside tuple)
nested = ("apple", ("banana", "cherry"), "orange")
print(nested[1][0])  

#Tuples operation
numbers = (1, 2, 3, 4, 5)

# Slicing
print(numbers[1:4])   # (2, 3, 4)

# Concatenation
more_numbers = numbers + (6, 7)
print(more_numbers)   # (1, 2, 3, 4, 5, 6, 7)

# Repetition
repeat = ("Hi",) * 3
print(repeat)         # ('Hi', 'Hi', 'Hi')


