name = input("Employee name: ")
salary = int(input("Employee Salary:"))
years = int(input("Employee years: "))

if years >=5:
    bonus = salary * 0.20
    total = salary + bonus
    print("\n---------Employee Details-------")
    print("Employee name:",name)
    print("Employee salary:",salary)
    print("Employee years:",years)
    print("Bonus is:",bonus)
    print("Total salary:",total)
    print("Status: Senior Employee")

else:
     bonus = salary * 0.10
     total = salary + bonus
     print("\n---------Employee Details-------")
     print("Employee name:",name)
     print("Employee salary:",salary)
     print("Employee years:",years)
     print("Bonus is:",bonus)
     print("Total salary:",total)
     print("Status: Junior Employee")