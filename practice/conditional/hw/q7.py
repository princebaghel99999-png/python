# Total number of even and odd number present in the list

numbers = [12,15,7,20,33,40,55]

e = 0
o = 0

for i in numbers:
    if i%2 ==0:
        e += 1
    else:
        o +=1


print("Total number of even number present in the list",e)

print("Total number of odd number present in the list",o)