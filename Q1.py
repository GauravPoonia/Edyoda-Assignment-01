# Q.1 - to capitalize 1st and last letter

string = input("Enter a string to capitalize : ")

string = string.title()

new = string.split()

new_string = ""
for i in new:
    new_string = new_string + i[:-1] + i[-1].upper() + ' '

print("The capitalize string is :",new_string[:-1])