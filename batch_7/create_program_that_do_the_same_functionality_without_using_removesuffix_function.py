#Prog02.Create a program that do the same functionality without using removesuffix() function.
#create def process similar to removesuffix function
#ask for user input
#print result

def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text