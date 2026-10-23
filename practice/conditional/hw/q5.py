# check the word is palindrome or not 

num= input("Enter word : ")

if num == num[::-1]:
    print("palindrome")
else:
    print("not palindrome")

