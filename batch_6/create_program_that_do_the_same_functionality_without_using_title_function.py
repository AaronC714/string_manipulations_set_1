#Prog10. Create a program that do the same functionality without using title() function.
#create def process for title function
#ask for user input
#print result

def title_case(text):
    words = text.split()
    result = []

    for word in words:
        # Capitalize the first letter of the word and make the rest lowercase
        result.append(word[0].upper() + word[1:].lower())

    # Join the words back together with spaces
    return ' '.join(result)

user_input = input("Enter a string: ")