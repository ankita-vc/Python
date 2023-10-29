# Variable is a container for a value which can be of various types

'''
This is multiline comment
or docstring(used to define function purpose)
can be in single or double quotes
'''

"""
VARIABLE RULES:
    - Variable names are case sensitive(name and NAME are different variables)
    - Must start with a letter or unserscore
    - Can have numbers but cannot start with numbers
"""

x= 1             #int
y= 4.6           #float
name= "Ankita"   #str
Condition= True  # bool

print(x)
print(y)
print(name)
print(Condition)

#Multiline Assignment
x, y, name, Condition= (1, 4.6, "Ankita", True)

print(x, y, name, Condition)

# Basic maths
a= x+y
print(a)

print(type(a))
print(type(x))
print(y, type(y))

# Casting

a= int(a)
y= str(y)

print(type(a))
print(y, type(y))

