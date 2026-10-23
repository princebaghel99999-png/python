w = int(input("enter number : "))
    
if w > 7000:
    print("Overloaded")
elif w > 4000:
    print("Time Estimated : 45 minutes")
elif w > 2000:
    print("Time Estimated : 35 minutes")
elif w > 0:
    print("Time Estimated : 25 minutes")
elif w == 0:
    print("Time Estimated : 0 minutes")
else:
    print("invalid input")

