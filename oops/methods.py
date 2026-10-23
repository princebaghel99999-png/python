class student:
    def __init__(self,name):
        self.n = name
    def show(self):
        print("hello college",self.n)
    def team(self,name1):
        print("welcome",self.n,name1)

data = student("ram")
data.show()
data.team("rohit")