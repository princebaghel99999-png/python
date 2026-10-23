# TYPES OF FUNCTIONS IN PYTHON
# Python me function ke types: Built-in, User-Defined, Lambda, Recursive,
# Generator, Nested, args, kwargs
# Built-in Functions Jo Python already provide karta hai

print("Hello")
print(len([1,2,3]))
print(type(10))
print(sum([10,20,30]))
print(max(5,8,2))


# user - defined function ke types (most important)
# No argument, no return
def hello():
    print("hello Python")
hello()

# Argument, No Return 
def add(a,b):
    print(a+b)
add(2,3)

# No argument, With Return 
def get_number():
    return 10
print(get_number()) 

# Argument, With Return
def add(a,b):
    return a+b
d= add(4,3)
print(d)