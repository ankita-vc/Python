# If/Else conditions are used to decide to do something based on something being true or false

x= 5
y= 5

# Comarision operators (== , != , > , < , >= , <= ) used to compare values

# simple if statement
if x > y:
    print(f'{x} is greater than {y}')

# if/else statement
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

# elif statement
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# nested if
if x > 2:
    if(x <= 10):
        print(f'{x} is greater than 2 and less tahn or equal to 10')

# Logical operators (and, or, not) used to combine conditional statements

# and
if x > 2 and x <= 10:  # both the statements have to be true
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:  # anyone of the statements have to be true
    print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not x == y:
    print(f'{x} is not equal to {y}')


# Men=mbership operators (in, not in) used to test if a sequence is present in an object or not (return true or false)

numbers= [1,2,3,4,5]

# in
if x in numbers:
    print(x in numbers)

# not in
if y not in numbers:
    print(y not in numbers) 


# Identity operators (is, is not) used to compare the objects, not if they are equal, but if they are actually the same objects with same memory location

# is
if(x is y):
    print(x is y)

if(x is not y):
    print(x is not y)
