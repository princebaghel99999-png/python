marks = int(input("enter marks: "))

if marks >=90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

    
email = "pn@gmail.com"
password = "123"
role = "user"

if email=="ram@gmail.com" and password=="123" and role =="admi":
    print("admin login successful")
elif email=="pn@gmail.com" and password=="123" and role =="user":
    print("user login successful")
else:
    print("login failed")


