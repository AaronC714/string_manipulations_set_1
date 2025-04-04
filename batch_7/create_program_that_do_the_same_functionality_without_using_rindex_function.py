#Prog10. Create a program that do the same functionality without using rindex() function.
#create def process for rindex function
#ask for user input
#print result

def custom_rindex(string, substring):
    for i in range(len(string) - len(substring), -1, -1):
        if string[i:i + len(substring)] == substring:
            return i
    raise ValueError(f"'{substring}' not found in the given string.")

string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

try:
    result = custom_rindex(string, substring)
    print(f"The last occurrence of '{substring}' is at index {result}.")
except ValueError as e:
    print(e)