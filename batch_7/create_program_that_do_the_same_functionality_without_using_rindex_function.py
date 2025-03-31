#Prog10. Create a program that do the same functionality without using rindex() function.
#create def process for rindex function
#ask for user input
#print result

def custom_rindex(string, substring):
    for i in range(len(string) - len(substring), -1, -1):
        if string[i:i + len(substring)] == substring:
            return i
    raise ValueError(f"'{substring}' not found in the given string.")