# Dictionary is a collection which is unordered, changable and indexed. No duplicate members

# Create a dictionary
person= {
    "first_name": "Ankita",
    "last_name": "Chavan",
    "age": 25
}

print(person)
print(type(person))

# using constructor

person2= dict(first_name= 'Ankita', last_name= "Chavan")
print(type(person2), person2)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key value
person["phone"]= '4564 4598 4599'
print(person)

# Get dict keys
print(person.keys())

# Get items
print(person.items())

# Copy dict
person3= person.copy()
print(person3)

person3['city']= "Pune"
print(person3)

# Remove item and pop
del person['age']
print(person)
person.pop('phone') 
print(person)

# Get length
print(len(person3))

# clear
person.clear()
print(person)



# list of dict 
people= [
    {'name': 'ankita', 'age': 30,},
    {'name': 'Shreya', 'age': 45}
]
print(people)

print(people[1])
print(people[0]['age'])