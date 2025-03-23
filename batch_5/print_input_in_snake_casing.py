# Ask user for input
full_name = input("Enter your full name: ")

# Format input into snake casing
snake_casing = full_name.lower().replace(" ", "_")

# Print the result
print("Output:", snake_casing)