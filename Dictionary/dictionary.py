# dictionary python ka ek data structure hai jo data ko
# key value pair mein store karta hai

#jaise kise student ki information

student = {
    "name":"Ravi",
    #"name":"Amit",  # duplicate key print nhi hoti
    "age":21,
    "course":"BCA"
}

# print(student)
# print(student["name"])


# mutable hai
# dictionary ko create karna ke baad update kar sakte hain.

student['age']=25

print(student)

# empty dictionary
data= {}

print(type(data))