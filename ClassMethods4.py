class Employee:

    raiseAmt= 1.05

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.mail= first + "." +last + "@gmail.com" 

    def FullName(self):
        print(self.first + self.last)

    def ApplyRaise(self):
        self.pay= int(self.pay * self.raiseAmt)

    @classmethod                       # we applying this method to the whole class (Class Method)
    def setRaiseAmount(cls, amount):
        cls.raiseAmt= amount

    @classmethod       # class method as a alternative constructor
    def FromString(cls, EmpStr):
        first, last, pay= EmpStr.split('-')
        return cls(first, last, pay)

    @staticmethod
    def IsWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

 """
 Monday= 0   Sunday= 6
  """       


emp1= Employee("Ankita", "Chavan", 50000)
emp2= Employee("Shreya", "Chavan", 60000)

import datetime   # date and time library

MyDate= datetime.date(2023, 10, 13)    # YY/MM/DD

print(Employee.IsWorkDay(MyDate))



""" 
regular method automatically pass self(object/instance) as first argument
class method automatically pass the cls(class) as first agrument
static method do not pass any agrument automatically
"""
   