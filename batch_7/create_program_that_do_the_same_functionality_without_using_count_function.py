#Prog08. Create a program that do the same functionality without using count() function.
#create def process for count function
#ask user input
#print result

def manual_count(text, target):
    count = 0
    
    for i in range(len(text) - len(target) + 1):
        if text[i:i+len(target)] == target:
            count += 1
            
    return count

user_input = input("Enter a string: ")
target_char = input("Enter the character or substring to count: ")

result = manual_count(user_input, target_char)
print(f"'{result}'")