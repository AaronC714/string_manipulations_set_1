#Prog06. Create a program that do the same functionality without using rjust() function.
#create def process for rjust function
#ask user input
#print result

def right_just(text, total_width):
    if not total_width.isdigit():
        return "Invalid input, must be an integer"
    
    total_width = int(total_width)

    if total_width <= len(text):
        return text
    
    return "_" * (total_width - len(text)) + text