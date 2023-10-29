# intialization of characteristics using constructor like funcrtion

class Employe:  # class 
    def __init__(self, first, last, pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first + '.' + last + '@gmail.com'

obj1= Employe('Ankita', 'Chavan', 50000)       # object creation with parameters(arbitary arguments)

obj2= Employe('Shreya', 'Chavan', 60000)

print(obj1.email)
print(obj2.email)
