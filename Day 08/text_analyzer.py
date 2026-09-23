# Day 08 - Text Analyzer

text = input("Enter a sentence: ")

# Number of characters
print("Number of characters:", len(text))

# Number of words
words = text.split()
print("Number of words:", len(words))

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Count vowels
vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

# Count spaces
print("Number of spaces:", text.count(" "))

# First and last character
if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])