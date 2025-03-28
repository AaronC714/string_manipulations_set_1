#Prog09. Create a program that do the same functionality without using capitalize() function.
#create def process for similar capitalize function
#ask for user input
#print result in capitalized form

def mimic_capitalize(text):
    if len(text) > 0:
        # Capitalize the first letter and make the rest lowercase
        return text[0].upper() + text[1:].lower()
    else:
        return text

user_input = input("Enter a string: ")