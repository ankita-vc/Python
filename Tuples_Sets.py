# Tuple is a collection which is ordered and unchangable. It allows duplicate members

# Create tuple
fruits= ("Apple", "Orange", "Grapes", "Pears")
print(fruits)

# with constructor
fruits2= tuple(("Apple", "Orange", "Grapes", "Pears"))
print(fruits2)

# Single value needs trailing comma, otherwise the type of variable is considered as string
fruits3= ("Apple")
print(fruits3, type(fruits3))

fruits4= ("Apple",)
print(fruits4, type(fruits4))

# Get a value
print(fruits[1])

# Change the value  (Tuples are unchangable)
#fruits[0]= "Pears"
#print(fruits)

# Delete tuple
del fruits2
#print(fruits2)

# length
print(len(fruits))




# Set is the collection which is unordered and unindexed. No duplicate members

# Create set
fruits_set= {"Apple", "Orange", "Grapes", "Pears"}
print(fruits_set)

# Check if in set
print("Apple" in fruits_set)

# Add to set
fruits_set.add("Straberries")
print(fruits_set)

fruits_set.add("Grapes")  # duplicates are not allowded
print(fruits_set)

# Remove from set
fruits_set.remove("Grapes")
print(fruits_set)

# Clear the set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
print(fruits_set)
