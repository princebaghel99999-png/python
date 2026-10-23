class Employee:
    pub = 8
    _protec =100
    __private = "vikas"


    def display(self):
        print(self.__private)

#access modifiers

a = Employee()
print(a.pub)
print(a._protec)
a.display()
# print(a.__private)