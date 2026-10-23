# print the total, avg and max sales from the list

sales = [1200,1500,900,2000,1800]

total = 0

for i in sales:
    total +=i
    
print("Total is :",total)

print("Average is ",total//len(sales))

print("Highest Sales is :",max(sales))