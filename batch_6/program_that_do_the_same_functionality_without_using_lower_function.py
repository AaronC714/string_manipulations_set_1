#Prog03. Create a program that do the same functionality without using lower() function.
#user input
#define and add lower case process
#print user input in lower case

user_input = str(input("Enter a text here: "))

def lower_case(user_input):
    result = " "

    for char in user_input:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

    return result
    
print (lower_case(user_input))