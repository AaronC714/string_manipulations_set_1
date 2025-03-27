#Prog04. Create a program that do the same functionality without using isupper() function.
#create process to identify if text is uppercased without using isupper()
#ask user for input
#print correct boolean


def is_upper_case(user_input):
    upper_count = 0
    lower_count = 0
    
    for count in user_input:
        if 'A' <= count <= 'Z':  #if the character is uppercase
            upper_count += 1
        elif 'a' <= count <= 'z':  #if the character is lowercase
            lower_count += 1
    if lower_count == 0:
        print("True")
    else:
        print("False")
        
user_input = input("Enter a text here: ")

#print result
print = (is_upper_case(user_input))