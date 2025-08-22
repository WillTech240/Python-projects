
for i in range(1, 12):
    print(f"{i} x {i} = {i* i}")

for row in range(8):         
    for col in range(8):     
        print("#", end=" ")  
    print()                  

for i in range(0,101):
    if i % 2 != 0:
        print(i)
sum = 0
for i in range(101):
    sum += i
    print(sum)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

# Loop from the last index to the first
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)
