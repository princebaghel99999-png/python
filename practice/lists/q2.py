# find the smallest element in a list

num = [10,15,8,13,20,18]

smallest = num[0]

for i in num[1:]:

    if i < smallest:
        smallest = i

print("Smallest element",smallest)