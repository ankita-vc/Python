class Employe:

    raiseAmt= 1.05

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.mail= first + "." +last + "@gmail.com" 

    def FullName(self):            # regular method
        print (self.first + self.last)

    def ApplyRaise(self):
        self.pay= int(self.pay * self.raiseAmt)

    @classmethod                       # we applying this method to the whole class (Class Method)
    def setRaiseAmount(cls, amount):
        cls.raiseAmt= amount


emp1= Employe("Ankita", "Chavan", 50000)
emp2= Employe("Shreya", "Chavan", 60000)

# Employe.raiseAmt= 1.05    instead of doing this we did that 
Employe.setRaiseAmount(1.04)  # Function call for class

print(Employe.raiseAmt)
print(emp1.raiseAmt)
print(emp2.raiseAmt)