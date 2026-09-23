# Day 08 - Palindrome Checker

text = input("Enter a word: ")

# Convert to lowercase
text = text.lower()

# Reverse the string
reverse_text = text[::-1]

print("Original:", text)
print("Reversed:", reverse_text)

if text == reverse_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")