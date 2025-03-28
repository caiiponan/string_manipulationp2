# Prompt for input text and the prefix to be removed
user_input = input("Enter a string: ")
prefix = input("Enter the prefix to be removed: ")

# Remove given prefix without using removeprefix() method
if user_input.startswith(prefix):
    user_input = user_input[len(prefix):]
    
# Print the string without the prefix 