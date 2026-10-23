with open("File Handling/student.txt",'r') as f:
    a = f.read()
print(a)

with open("File Handling/student.txt",'w') as f:
    a = f.write("hello gwalior")
print(a)