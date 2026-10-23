class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def team(self):
        print(self.name)

    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}"
    #object ko human readable string me convert karta hai

data = user("ram",45)
# data.team()
print(data)  #