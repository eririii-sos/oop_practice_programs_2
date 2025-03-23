# Ask user for input
characters = input("Enter any statement or word(s): ")

# Count number of characters without including the spaces
character_count = len(characters.replace(" ", ""))

# Print the result
print("Characters count:", character_count)