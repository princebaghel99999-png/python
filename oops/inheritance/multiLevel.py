class Person:
    country = "India"

    def takeBreath(self):
        print("gwalior")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print("salary 10000")
    def takeBreath(self):
        super().takeBreath()
        print("pninfosys")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):

        print(f"No salary to progrmmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an programmer so i am luckily breathing++...")


p = Programmer()
p.takeBreath()
