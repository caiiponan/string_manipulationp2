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
for char in user_input[1:]:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char

# Print the result
print(result)