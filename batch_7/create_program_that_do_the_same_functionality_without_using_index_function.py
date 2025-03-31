#Prog09. Create a program that do the same functionality without using index() function.
#create def process similar to index function
#ask user input
#print result

def custom_index(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            return i
    raise ValueError(f"'{substring}' not found in the given string.")

user_input = input("Enter the main string: ")
index_search = input("Enter the substring to find: ")