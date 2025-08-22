print("\nTuples")
my_tuple = ("red", "green", "blue", "green", "yellow")
print(f"Initial Tuple: {my_tuple}")

# 1. Access Tuple Items
print(f"Element at index 0: {my_tuple[0]}")
print(f"Elements from index 1 to 3: {my_tuple[1:4]}")

# 2. Attempt to Change Tuple Items
print("Attempting to change tuple items will result in a TypeError because tuples are immutable.")

# 3. Loop Through a Tuple
print("Looping through tuple:")
for item in my_tuple:
    print(item)

# 4. count() Operation
green_count = my_tuple.count("green")
print(f"Count of 'green': {green_count}")

# 5. index() Operation
blue_index = my_tuple.index("blue")
print(f"Index of 'blue': {blue_index}")

# 6. Length of a Tuple
tuple_length = len(my_tuple)
print(f"Length of the tuple: {tuple_length}")
