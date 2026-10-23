# l = [10,20,30,40]
# print(len(l))
# s = "welcome"
# print(len(s))

#overridding

class pn:
    def diplayinfo(self):
        print("welcome to pninfosys")
class itm(pn):
    name ="ram"
    # def diplayinfo(self):
    #    print("welcome to pninfosys") 

obj = itm()
obj.diplayinfo()

#overloading
class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing")

obj1 =Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)


#overriding
class A:
    def showData(self):
        print("i m in A class")
class B(A):
    def showData(self):
        # return super().showData()
         print("i m in B class")

obj = B()
obj.showData()
    