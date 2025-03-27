#Prog05. Create a program that do the same functionality without using endswith() function.
#process of determining if input and prameter are the same
#user inputs (statment and wanted parameters)
#print result, true or false

def ends_with(text, suffix):
    return text[-len(suffix):] == suffix if len(suffix) <= len(text) else False

user_input = input("Enter a string: ")
suffix_input = input("Enter the suffix to check: ")