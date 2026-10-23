
class papa:
    bike = "007"

    def showDetails(self):
        print("This is an employee")

class son(papa):
    language = "python"
    bike ="008"

    def getLanguage(self):
        print(f"The language is{self.language}")
    def showDetails(self):
        print("this is an programmer")

p = son()
print(p.bike)
p.showDetails()
p.getLanguage()