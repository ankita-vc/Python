class Employee:

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

    @classmethod       # class method as a alternative constructor
    def FromString(cls, EmpStr):
        first, last, pay= EmpStr.split('-')
        return cls(first, last, pay)


emp1= Employee("Ankita", "Chavan", 50000)
emp2= Employee("Shreya", "Chavan", 60000)

empStr1= 'Ram-Thakur-40000'  
empStr2= 'Nisha-Kadam-70000'
empStr2= 'Jane-Doe-80000'
 
newEmployee1= Employee.FromString(empStr1) 

print(newEmployee1.first)
print(newEmployee1.pay)

