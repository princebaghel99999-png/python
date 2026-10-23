# class student:
#     __name = "ravi" # private variable direct object ke sath use nahi hota

#     def __init__(self):   # constructor ki help se call kar sakte hai
#         print(self.__name) 
#         self.__displayinfo()

#     def __displayinfo(self): # private
#         print("hello gwalior")

#     def itm(self):
#         self.__displayinfo()
#         print(self.__name)

# obj = student()
# # print(obj.__name)
# obj.itm()


# encapsulation getter and setter

class Students:
    def __init__(self):
        self._name =""

    def getname(self):
        return self._name

    def setname(self,name):
        self._name = name


obj = Students()
obj.setname("raj")
# obj.setname("kumar")
name = obj.getname()
print(name)