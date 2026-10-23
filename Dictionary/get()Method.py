#agar key na mile to error nahi aata.

student = {
    "name":"ravi",
    "age":21
}

# print(student.city)
print(student.get("city"))
student["city"] = "ahemdabad"  # add
student["age"] = 25   # update
student.pop("age")   # remove
student.clear()

print(student)