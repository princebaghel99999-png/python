
class Employee:
    car = "pninfosys"
    ecode = 120

class Freelancer:
    car = "google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):

    name = "vikas"


p = Programmer()
print(p.car)
p.upgradeLevel()
print(p.level)