#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#ask user for full name with spaces before the name
#process result without using lstrip()
#print result

user_name = input("Enter your name with multiple spaces before it (ex.     Juan Dela Cruz): ")

def remove_leading_spaces(user_name):
    index = 0
    while index < len(user_name) and user_name[index] == ' ':
        index += 1
    return user_name[index:]