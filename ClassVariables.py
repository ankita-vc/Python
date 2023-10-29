class Employe:

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + "." + last + "@gmail.com"

    def FullName(self):
        printf(self.first + self.last)

    def PayRaise(self):
        self.pay= int(self.pay * 1.04)   # Payment increased by 4%


obj1= Employe("Ankita", "Chavan", 50000)
obj2= Employe("Shreya", "Chavan", 60000)
obj3= Employe("Ram", "Bhor", 40000)

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)

print(obj1.pay)
obj1.PayRaise()
print(obj1.pay)