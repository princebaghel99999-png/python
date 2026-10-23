A = {4,5}
B = {3,4}

print(A.union(B)) # A or B
print(A.intersection(B)) 
print(A.difference(B))
print(A.symmetric_difference(B))
print(A & B)  # common elements
print(A | B) # union


# list ko set mein convert karna
# duplicate data remove karna
numbers = [10,20,20,30,30,40]

unique = set(numbers)

print(unique)