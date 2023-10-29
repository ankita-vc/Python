''' 
Function is a block of code which only runs when it is called.
In python, we do not use curly brackets, we use indentation with tabs or spaces
'''

# Create a function

def sayHello(name):   # helper function 
    print(f'hello, {name}')

sayHello('ankita chavan') # function call


def Display(name= 'Ankita'):  # function with default argument
    print(f"Namaskar, {name}")

Display()  # Function call with no argument


# Return value

def Addition(iNo1, iNo2):
    Ans= iNo1 + iNo2
    return Ans

iRet= Addition(10, 30)
print(iRet)

'''
lambda function is a small anonymous function
it can take any number of arguments, but can only have one expression,
exacrly similar to JS arraow function
'''

# Function         Arguments     function body
Addition=  lambda  iNo1, iNo2 :  iNo1 + iNo2

print(Addition(20, 50))
