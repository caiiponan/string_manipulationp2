# Prompt user for input
user_input = input("Enter a string: ")

# Set fixed width for the output
width = 50

# Add spaces to the right of the string to reach the fixed width
add_spaces = width - len(user_input)

if add_spaces > 0:
    user_input += " " * add_spaces

# Print the string with added spaces
print(user_input)