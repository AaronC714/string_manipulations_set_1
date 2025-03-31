#Prog07. Create a program that do the same functionality without using zfill() function.
#create def process for zfill function
#ask user input
#print result

def zero_fill(number, total_width):
    if not total_width.isdigit():
        return "Invalid input, must be an integer"
    
    total_width = int(total_width)
    
    if total_width <= len(number):
        return number
    
    return "0" * (total_width - len(number)) + number