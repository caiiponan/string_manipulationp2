# Prompt user input
user_input = input("Enter a string with leading whitespaces: ")

# Initialize a variable to store the index of the first non-whitespace character
index = 0

# Remove leading whitespaces without using lstrip() method
while index < len(user_input) and user_input[index] == " ":
    index += 1
user_input = user_input[index:]

# Print the string without leading whitespaces