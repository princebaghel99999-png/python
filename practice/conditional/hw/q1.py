# number is divisible by 3 and 5 or both 

i= int(input("Enter number : "))


if i % 3 ==0 and i%5 ==0:
    print("Divisible by both")
elif i%3 == 0 :
    print("Divisible by 5")
elif i%5 ==0 :
    print("Divisible by 3")

