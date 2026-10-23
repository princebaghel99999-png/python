# *args(tuple) multiple positional arguments
def add_number(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(add_number(10,20,30,40))

# **kwargs(Dictionary) multiple keyword arguments
def student_info(**data):
    print(data)

student_info(name="Vikas", course="Python", fees=5000)
