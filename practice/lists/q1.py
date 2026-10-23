# find the largest element in a list

num = [10,15,8,13,20,18]
# num = []


if len(num)==0:
    print("List is empty")
else:
    largest = num[0]

    for i in num[1:]:

        if i > largest:
            largest = i
        
print("largest element is",largest)