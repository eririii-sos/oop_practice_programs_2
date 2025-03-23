# Ask user for input
full_name = input("Enter your full name in random casing format: ")

# Format input in pascal case 
pascal_casing = full_name.title().replace(" ", "")

# Print the result
print("Output:", pascal_casing)