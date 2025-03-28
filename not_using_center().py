# Prompt user for input
user_input = input("Enter a string: ")

# Set fixed width for the output
width = 50

# Add spaces to both sides of the string to reach the fixed width
spaces = width - len(user_input)
if spaces > 0:
    left_space = spaces // 2
    right_space = spaces - left_space
    user_input = " " * left_space + user_input + " " * right_space

# Print the string with added spaces