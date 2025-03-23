# Ask user for input
number = int(input("Enter a number (0-1000): "))

# Format input into 6 digits
formatted_number = f"{number:06d}"

# Print result
print("Output:", formatted_number)