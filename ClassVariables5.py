# Flow of code

class Employe:

    print("Class")
    RaiseAmount= 1.04    # Class Variabls
    EmployeCount= 0

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + "." + last + "@gmail.com"

        Employe.EmployeCount += 1

    def FullName(self):
        printf(self.first + self.last)

    def PayRaise(self):
        self.pay= int(self.pay * self.RaiseAmount)   # with referance to object


print("Main")
print(Employe.EmployeCount)

obj1= Employe("Ankita", "Chavan", 50000)
obj2= Employe("Shreya", "Chavan", 60000)
obj3= Employe("Ram", "Bhor", 40000)

print(Employe.EmployeCount)
