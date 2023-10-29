# String in python are surrounded by either single or double quotes

name= "Ankita"
age= 23


# STRING FORMATTING

#Concatenate
# print("Hello, I am " + name + "and I am " + age)

print("Hello, I am " + name + " and I am " + str(age))

#Arguments by position
print("My name is {name} and I am {age}". format(name= name, age= age))

# F-strings (only available in python version 3.6+)
print(f"hello, my name is {name} and I am {age}")



# STRING METHODS

s= "Hello World"

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace("World", "Everyone"))

# Count
sub= 'l'
print(s.count(sub))

print(s)

# Starts with  return true or false
print(s.startswith("Hello"))

# Ends with   return true or false
print(s.endswith("d"))

# Split into a list
print(s.split())

# Find Position
print(s.find('o'))

# Is all alphanumeric  return true or false
print(s.isalnum())

# Is all alphabetic   return true or false
print(s.isalpha())   #it will return false because of the space

# Is all numeric   return true or false
print(s.isnumeric())
