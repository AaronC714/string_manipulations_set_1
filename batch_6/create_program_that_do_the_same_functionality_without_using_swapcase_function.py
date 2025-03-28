#Prog08. Create a program that do the same functionality without using swapcase() function.
#create def process similar to swapcase function
#ask for user input
#print result in swapped case

def swap_case(user_input):
    result = ""

    for char in user_input:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    return result