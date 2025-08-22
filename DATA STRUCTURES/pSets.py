print("\nPart 3: Sets")
my_set = {"apple", "banana", "cherry", "apple", "date"}
print(f"Initial Set: {my_set}")

# 1. add() Operation
my_set.add("grape")
print(f"After add('grape'): {my_set}")

# 2. remove() Operation
my_set.remove("banana")
print(f"After remove('banana'): {my_set}")

# 3. Length of a Set
set_length = len(my_set)
print(f"Length of the set: {set_length}")

# 4. Membership Test
is_cherry_in_set = "grape" in my_set
print(f"Is 'cherry' in the set? {is_cherry_in_set}")
is_mango_in_set = "mango" in my_set
print(f"Is 'mango' in the set? {is_mango_in_set}")

# 5. pop() Operation
popped_set_item = my_set.pop()
print(f"After pop(): {my_set}, Popped Item: {popped_set_item}")

# 6. clear() Operation
my_set.clear()
print(f"After clear(): {my_set}")