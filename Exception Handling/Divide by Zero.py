try:
    a = int(input("Enter first number: "))
    b = int(input("Enter Second number: "))

    print('Result: ',a/b)

except ZeroDivisionError:
    print("Error: cannot divide by zero")

# zerodivisionerror ek built-in exception hai jo tab raise hota
# hai jab kisi number ko 0 se divide karne ki 
#koshish ki jaati hai.