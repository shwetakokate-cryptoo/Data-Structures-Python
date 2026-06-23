# ==========================================
# Array Basics in Python
# ==========================================

# Arrays are used to store multiple values
# in a single variable.
#
# In Python, lists are commonly used as arrays.

# ------------------------------------------
# Creating an Array (List)
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

# ------------------------------------------
# Display Array
# ------------------------------------------

print("Original Array:")
print(numbers)

# ------------------------------------------
# Access Elements
# ------------------------------------------

print("\nFirst Element:", numbers[0])
print("Last Element :", numbers[-1])

# ------------------------------------------
# Add Element
# ------------------------------------------

numbers.append(60)

print("\nAfter Adding 60:")
print(numbers)

# ------------------------------------------
# Remove Element
# ------------------------------------------

numbers.remove(20)

print("\nAfter Removing 20:")
print(numbers)

# ------------------------------------------
# Traverse Array
# ------------------------------------------

print("\nTraversing Array:")

for number in numbers:
    print(number)

