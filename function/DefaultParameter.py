def hello(name="Guest"):
    print("Hello",name)

hello()
hello("Prince")

# keyword arguments
def student(name,age):
    print(name,age)

student(age=20, name="Rahul")

# Variable-Length Arguments
def total(*nums):
    print(sum(nums))

total(10,20,30,40)
