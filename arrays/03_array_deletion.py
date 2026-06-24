# ==========================================
# Array Deletion in Python
# ==========================================

# This program demonstrates different
# ways of deleting elements from an array.

# ------------------------------------------
# Initial Array
# ------------------------------------------

numbers = [10, 20, 30, 40, 50, 60]

print("Original Array:")
print(numbers)

# ------------------------------------------
# Remove by Value
# ------------------------------------------

numbers.remove(30)

print("\nAfter Removing Value 30:")
print(numbers)

# ------------------------------------------
# Remove by Index using pop()
# ------------------------------------------

removed_element = numbers.pop(2)

print(f"\nRemoved Element: {removed_element}")
print("Array After pop(2):")
print(numbers)

# ------------------------------------------
# Remove Last Element
# ------------------------------------------

last_element = numbers.pop()

print(f"\nRemoved Last Element: {last_element}")
print("Array After pop():")
print(numbers)

# ------------------------------------------
# Delete using del
# ------------------------------------------

del numbers[1]

print("\nAfter del numbers[1]:")
print(numbers)

# ------------------------------------------
# Final Array
# ------------------------------------------

print("\nFinal Array:")
print(numbers)
