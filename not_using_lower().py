# Prompt user for input
user_input = input("Enter a string with capital letters: ")

# Initialize a variable to store the result
result = ""

for char in user_input:
# Check if character is uppercase letter
    if 'A' <= char <= 'Z':
        # Convert to lowercase by adding 32 to ASCII value
        result += chr(ord(char)) + 32)
    else:
        result += char
# Output with lowercase characters
