#Prog06. Create a program that do the same functionality without using ljust() function.
#create def for same functionality as ljust function
#ask for user's input
#print result

def left_just(text, num_spaces):
    if not num_spaces.isdigit():
        return "Invalid input, must be an integer"
    
    return text + "_" * int(num_spaces)

user_input = str(input("Enter a statement: "))
add_spaces = (input("Input how many spaces you would like after your initial input: "))