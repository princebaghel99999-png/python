# find the second smallest element in a list

num = [10,15,8,13,20,18]

smallest = num[0]
second_smallest = float('inf')

for i in num[1:]:

    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i > smallest and i < second_smallest:
        second_smallest = i

print("Second smallest element",second_smallest)