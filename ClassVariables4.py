class Employe:

    RaiseAmount= 1.04    # Class Variabls

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + "." + last + "@gmail.com"

    def FullName(self):
        printf(self.first + self.last)

    def PayRaise(self):
        self.pay= int(self.pay * self.RaiseAmount)   # with referance to object


obj1= Employe("Ankita", "Chavan", 50000)
obj2= Employe("Shreya", "Chavan", 60000)
obj3= Employe("Ram", "Bhor", 40000)

print(obj1.RaiseAmount)
print(obj2.RaiseAmount)
print(obj3.RaiseAmount)

obj2.RaiseAmount = 1.05   ##

print(obj1.pay)
obj1.PayRaise()
print(obj1.pay)

print(obj1.RaiseAmount)
print(obj2.RaiseAmount)
print(obj3.RaiseAmount)