# # String characters ka collection hota hai.
# # String immutable hota hai. means ham isse change nahi kar sakte

# name = "PNINFOSYS"

# print(name)
# print(name[0])
# print(name[1])

# # name[0] = 'J' # String is immutable,therefore we can't change the value of string
# # print(name) # TypeError: 'str' object does not support item assignment

# name = name + " Softwares"
# print(name) # concatention

# Slicing

# name = "PNINFOSYS"

# print(name[0:4]) # start with 0 and end with 3
# print(name[4:7]) # start with 4 and end with 6
# print(name[:]) # All characters
# print(name[:7]) # first 7 character
# print(name[4:]) # from index 4 to end
# print(name[-3:]) # last 3 character
# print(name[::-1]) # reverse the string
# print(name[0:9]) # from index 0 to last 2 character

# Useful String Methods

name = "pninfosys is"

print(len(name))
print(name.upper())
print(name.lower())
print(name.count("n")) #count occurrence of a character
print(name.find("n")) # find the index of a character
print(name.replace("n","X")) # replace a character
print(name.strip()) # remove leading/trailing whitespace
print(name.split()) # split the string into a list
name1= ["pninfosys","is","er"]
print(name.join(name1)) # join a list into a string
print(name.title()) # Convert to title case
print(name.capitalize())