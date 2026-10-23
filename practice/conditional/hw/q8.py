# Second largest number in the list

nums = [10,5,22,8,19]

largest = nums[0]

second_largest = float('-inf')

for i in nums[1:]:

    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i


print("Second largest number in the list is",i)