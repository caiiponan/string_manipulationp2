# Prompt user for input
user_input = input("Enter a string: ")

# Initialize the result string as an empty string
result = ""

# Flag to decide when to capitalize
make_capital = True

# Check if every next character is uppercase
for char in user_input:
    if char == ' ':
        result += char
        make_capital = True
        
# Make it uppercase
# Make it lowercase
# Print title-cased result