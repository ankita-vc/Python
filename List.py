# List is the collection variables which are stored in a order and can be changed. List allows duplicate members

""" 
Indexing in list starts from 0 as like array.

"""
# Create list
numbers= [1,2,3,4,5] 
fruits= ["Apple", "Orange", "Grapes", "Pears"]

# Use a constructor
numbers2= list((1,2,3,4,5))
print(numbers, numbers2)

# Get a value
print(fruits[3])

# Get length
print(len(fruits))

# Append to List
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove("Grapes")
print(fruits)

# Insert at position
fruits.insert(2, "Strawberries")
print(fruits)

# Change value
fruits[0]= "Blueberries"
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Sort the list in reverse order
fruits.sort(reverse= True)
print(fruits)


