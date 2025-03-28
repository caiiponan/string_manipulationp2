# Prompt user for input
user_input = input("Enter a string: ")

# Initialize an empty string
result = ""

# Loop through the input string
for char in user_input:
# If the character is lowercase
    if 'a' <= char <= 'z':
    # Convert to uppercase
        result += chr(ord(char) - 32)
# Elif the character is uppercase
    elif 'A' <= char <= 'Z':
    # Convert to lowercase
        result += chr(ord(char) + 32)
# Else keep non-alphabetic characters as they are
    else:
        result += char
# Print the converted string
print(result)