#Statistics Module
from statistics import mean, median, mode, stdev

ages = [20, 20, 24, 24, 25, 22, 26, 20, 23, 22, 26]

print("STATISTICS MODULE")
print("Ages:", ages)
print("Mean:", mean(ages))
print("Median:", median(ages))
print("Mode:", mode(ages))
print("Standard Deviation:", stdev(ages))
print()


# MATH MODULE
import math

print("MATH MODULE")
print("Pi:", math.pi)
print("Square root of 2:", math.sqrt(2))
print("2 to the power 3:", math.pow(2, 3))
print("Floor of 9.81:", math.floor(9.81))
print("Ceil of 9.81:", math.ceil(9.81))
print("Log base 10 of 100:", math.log10(100))
print()


# STRING MODULE
import string

print("STRING MODULE")
print("ASCII Letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)
print()


# RANDOM MODULE
from random import random, randint, uniform, randrange, choice, choices, shuffle, seed

print("RANDOM MODULE")
print("Random float (0.0 - 1.0):", random())
print("Random integer (5 - 20):", randint(5, 20))
print("Random float (1 - 10):", uniform(1, 10))
print("Random even number (0 - 18):", randrange(0, 20, 2)) #start=0 #stop=20 #step=2

# Random choice from a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit (choice):", choice(fruits))
print("Random fruits (choices, k=2):", choices(fruits, k=2))

# Shuffle the list
shuffle(fruits)
print("Shuffled fruits:", fruits)

# Using a seed 
seed(5)
print("With seed 5, random integer (1-10):", randint(1, 10))
