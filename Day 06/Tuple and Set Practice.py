numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of tuple:", len(numbers))

# Set
number_set = {10, 20, 30, 30, 40, 40, 50}

print("\nSet:", number_set)
print("Length of set:", len(number_set))

# Add an element
number_set.add(60)
print("After adding 60:", number_set)

# Remove an element
number_set.remove(20)
print("After removing 20:", number_set)

# Check whether an element exists
if 30 in number_set:
    print("30 is present in the set")
else:
    print("30 is not present in the set")