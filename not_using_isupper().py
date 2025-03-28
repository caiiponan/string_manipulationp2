# Prompt user for input
user_input = input("Enter a string: ")

# Assume the user will enter a string with capital letters
all_uppercase = True

for char in user_input:
# Find lowercase letters and set to false
    if 'a' <= char <= 'z':
        all_uppercase = False
        break

# Print result if all uppercase is true or false.
if all_uppercase:
    print("All characters are uppercase.")
else:
    print("Not all characters are uppercase.")