#Prog01. Create a program that do the same functionality without using rstrip() function.
#create def process for rstrip
#ask for user input
#print result

def remove_latter_spaces(user_name):
    index = -1 
    while index >= -len(user_name) and user_name[index] == ' ':
        index -= 1
    return user_name[:index + 1]