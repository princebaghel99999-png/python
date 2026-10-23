f = open("File Handling/student.txt",'w')

student = [
    "123\n",
    "456\n",
    "789\n"
]

f.writelines(student)
f.close()
