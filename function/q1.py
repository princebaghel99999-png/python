N = 10
k=5

number =int(input("enter number:"))

if number > N:
    print("invalid input") 
else:
    N -= number
    print("number of candies sold : ",number)
    print("number of candies available : ",N)

