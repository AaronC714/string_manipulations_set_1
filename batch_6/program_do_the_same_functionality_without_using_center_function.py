#Prog07. Create a program that do the same functionality without using center() function.
#create def process that replicates center function
#ask for user input
#print result

def center_function(text, char, length):
    if not length.isdigit():
        return "Invalid input, length must be an integer"

    if len(text) >= length:
        return text
    
    total_padding = length - len(text)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    return char * left_padding + text + char * right_padding

user_input = input("Enter a text: ")
character_choice = input("Type character you want to use: ")
total_length = input("How long do you want the result to be: ")