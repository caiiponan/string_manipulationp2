# Prompt user for input text
user_input = input("Enter a string: ")

# Let user specify if the text ends with the suffix
suffix = input("Enter the suffix to check: ")

# Get the length of the suffix
suffix_length = len(suffix)

# Compare the end part of the text with the suffix and print the result
if user_input[-suffix_length:] == suffix:
    print("True")
else:
    print("False")