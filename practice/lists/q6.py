# reverse a list 

num = [10,20,30,40,50]

# reverse = []


# for i in range(len(num)-1,-1,-1):
#     reverse.append(num[i])

# print(reverse)

l=0
r=len(num)-1

while l < r:
   
    num[r],num[l] = num[l],num[r]
    l +=1
    r -=1


print(num)


    
