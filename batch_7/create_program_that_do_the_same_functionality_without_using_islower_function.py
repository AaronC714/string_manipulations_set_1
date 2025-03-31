#Prog04. Create a program that do the same functionality without using islower() function.
#create def process for islower function
#ask user input
#print result

def is_lower(text):
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

user_input = input("enter a string: ")
lower_function = is_lower(user_input)
print (lower_function)