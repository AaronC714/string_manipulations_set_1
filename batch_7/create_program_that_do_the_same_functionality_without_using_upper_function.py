#Prog03. Create a program that do the same functionality without using upper() function.
#create def process for upper function
#ask user input
#print result

def upper_case(text):
    result = " "

    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result