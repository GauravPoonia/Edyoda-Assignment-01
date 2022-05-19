# Q.2 - to find no of vowels in a string

str = input("Enter a string : ")

count = 0
for i in str:
    if i in ("a","e","i","o","u"):
        count += 1
        
print("Vowels :",count)