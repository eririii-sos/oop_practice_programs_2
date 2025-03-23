# Ask user for input
characters = input("Enter your full name: ")

# Count number of characters without including the spaces
character_count = len(characters.replace(" ", ""))

# Print the result
print("Characters count:", character_count)