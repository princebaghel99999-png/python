f = open('File Handling/student.txt')

t = f.read()
if 'pninfosys' in t:
    print("present")
else:
    print("not present")

f.close()