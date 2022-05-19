# Q.3 - to find string has special characters or not

lst = '[@_!#$%^&*()<>?/\|}{~:]'

str = input("Enter a string : ")

for i in str:
    if i in lst:
        print("String is not accepted")
        break
else:
    print("String is accepted")