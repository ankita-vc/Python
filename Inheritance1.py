class Employee:

    RaiseAmount= 1.04

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + "." + last + "@gmail.com"

    def FullName(self):
        return (f"{self.first} {self.last}")

    def SaleryRaise(self):
        return int(self.pay * self.RaiseAmount) 
        
    
Emp1= Employee("Ankita", "Chavan", 60000)
Emp2= Employee("Shreya", "Rao", 70000)
Emp3= Employee("Tara", "Paul", 80000)

print(Emp1.first)
print(Emp2.email)
print(Emp3.FullName())

print(Emp2.SaleryRaise()) 