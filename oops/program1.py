class user:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name,self.marks)

s = user("rahul",30)
s.show()
