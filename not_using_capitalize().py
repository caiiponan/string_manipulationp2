# Prompt user for input
user_input = input("Enter a string: ")

# Initialize an empty string to store the result
result = ""

# Convert first character to uppercase 
if len(user_input) > 0:
    first_letter = user_input[0]
    if 'a' <= first_letter <= 'z':
        first_letter = chr(ord(first_letter) - 32)
    result += first_letter

# Convert the rest to lowercase
# Print the result