#Prog02. Create a program that do the same functionality without using removeprefix() function.
#user input name
#process in removing prefix under desired parameter
#print user name after process

def remove_prefix(text, prefix):
    if text.startswith(prefix):  #If the string starts with the given prefix
        return text[len(prefix):]  #Remove prefix by slicing
    return text  # Return the original string if prefix is not found

user_name = str(input("Enter your name: "))
parameters = str(input("Enter prefix to remove: "))