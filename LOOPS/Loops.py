#While loop
count = 0
while count < 5:
    if count == 4:
        count += 1
        continue
    elif count != 2:
        count += 1
        continue
    print(count)
    count += 1

    #for loop
    #for iterator in range()
    numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    print(number)

    


language = 'Python'
for letter in language:
    print(letter)
numbers = (1,2,3,4,5)
for i in numbers:
    print(i)
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) 

    lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# syntax
#for iterator in range(start, end, increment):