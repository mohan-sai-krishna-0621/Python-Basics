#  String Practice

name = "Mohan Krishna"

print("Original string:", name)

# Length
print("Length:", len(name))

# First character
print("First character:", name[0])

# Last character
print("Last character:", name[-1])

# Slicing
print("First 5 characters:", name[:5])
print("Last 7 characters:", name[-7:])

# Uppercase and lowercase
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# Replace
print("After replace:", name.replace("Mohan", "Hello"))

# Check if word exists
print("Is 'Krishna' present?", "Krishna" in name)