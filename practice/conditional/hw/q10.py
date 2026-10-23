# cube of odd number using dictionary comprehension

cubes = {x: x**3 for x in range(1,26) if x%2!=0}

print(cubes)