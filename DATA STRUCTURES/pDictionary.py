print("\nDictionaries")
my_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red"
}
print(f"Initial Dictionary: {my_dictionary}")

# 1. Access Specific Value by Key
model_name = my_dictionary["model"]
print(f"Model: {model_name}")
year_value = my_dictionary["year"]
print(f"Year: {year_value}")

# 2. Access Keys, Values, and Items
all_keys = my_dictionary.keys()
print(f"All Keys: {list(all_keys)}")
all_values = my_dictionary.values()
print(f"All Values: {list(all_values)}")
all_items = my_dictionary.items()
print(f"All Items: {list(all_items)}")

# 3. Add/Change Dictionary Items
my_dictionary["engine"] = "V8"
print(f"After adding 'engine': {my_dictionary}")
my_dictionary["color"] = "blue"
print(f"After changing 'color': {my_dictionary}")

# 4. Remove Dictionary Items
removed_year = my_dictionary.pop("year")
print(f"After pop('year'): {my_dictionary}, Removed Year: {removed_year}")
del my_dictionary["brand"]
print(f"After del my_dictionary['brand']: {my_dictionary}")

# 5. Length of a Dictionary
dictionary_length = len(my_dictionary)
print(f"Length of the dictionary: {dictionary_length}")

# 6. clear() Operation
my_dictionary.clear()
print(f"After clear(): {my_dictionary}")