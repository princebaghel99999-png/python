# Set Python ka ek collection data type hai jo unique values store karta hai.

# Duplicate values automatically remove ho jati hain.
# Indexing nahi hoti.
# Unordered collection hai (items ka order fixed nahi hota).
# Mutable hai (add/remove kar sakte hain).

numbers = {10,20,30,20,10}

# print(numbers)   # 20 10 30 (order change ho sakta hai) duplicate values allowed nahi hai
# numbers.add(40)
# print(numbers)  # 20 10 30 40 (add karta hai ) mutable hai
# print(numbers[0])   # index nahi hota


# empty set banana
# s= {1,}  # dictionary hai
# s= {1}
# s = set()  # set hai
# print(type(s))

#set mein item add karna
#add()

# fruits = {"Apple","mango","ram"}

# fruits.add("banana")
# fruits.add("abc")
# fruits.update(["ram","banana123"])
# fruits.remove("mango")
# fruits.discard("Orange")  # remove karta hai error nahi deta
# fruits.pop()
# # fruits.clear()  # remove all items

# print(fruits)

# loop in set 
fruits = {"apple","mango","banana"}

for fruit in fruits:
    print(fruit)