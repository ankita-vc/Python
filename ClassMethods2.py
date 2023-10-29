class Employe:

    raiseAmt= 1.05

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.mail= first + "." +last + "@gmail.com" 

    def FullName(self):
        print (self.first + self.last)

    def ApplyRaise(self):
        self.pay= int(self.pay * self.raiseAmt)

    @classmethod                       # we applying this method to the whole class (Class Method)
    def setRaiseAmount(cls, amount):
        cls.raiseAmt= amount


emp1= Employe("Ankita", "Chavan", 50000)
emp2= Employe("Shreya", "Chavan", 60000)


# employee names are provided in the string so firstly we have to split the string into first last and pay
empStr1= 'Ram-Thakur-40000'  
empStr2= 'Nisha-Kadam-70000'
empStr2= 'Jane-Doe-80000'

first, last, pay= empStr1.split('-')  # inbuilt method to split the string

newEmployee1= Employe(first, last, pay)  # pass those splitted values to the class for furher operations

print(newEmployee1.first)
print(newEmployee1.pay)

