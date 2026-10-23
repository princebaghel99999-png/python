# count the total number of vowel and consonant is present in the string

word = "PrinceBaghel"

v = 0
c = 0

for i in word:
    if i in "aeiouAEIOU":
        i=1
        v += i
    else:
        i =1
        c +=1

     
print(" Total number of vowel present are",v)  

print("Total number of consonant present are",c)