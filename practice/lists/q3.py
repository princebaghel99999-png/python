# find the second largest element in a list

# num = [10,15,8,13,20,18]
# num = [10]
num = [5,5,5,5]

largest = num[0]
second_largest = float('-inf')


for i in num[1:]:

    if i > largest:
        second_largest = largest
        largest = i
    elif i < largest and i > second_largest:
        second_largest = i


print("Second Largest element",second_largest)
