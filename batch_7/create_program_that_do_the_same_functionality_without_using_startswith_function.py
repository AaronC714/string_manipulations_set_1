#Prog05.  Create a program that do the same functionality without using startswith() function.
#create def process for startswith function
#ask for user inputs
#print final results

def starts_with(text, prefix):
    return text[:len(prefix)] == prefix

user_input = input("Enter a string: ")
start_choice = input("Prefix to check: ")

final_prefix = starts_with(user_input, start_choice)
print (final_prefix)