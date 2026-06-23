# ==========================================
# Array Insertion in Python
# ==========================================

# This program demonstrates different
# ways of inserting elements into an array.

# ------------------------------------------
# Initial Array
# ------------------------------------------

numbers = [10, 20, 30, 40]

print("Original Array:")
print(numbers)

# ------------------------------------------
# Insert at Beginning
# ------------------------------------------

numbers.insert(0, 5)

print("\nAfter Inserting 5 at Beginning:")
print(numbers)

# ------------------------------------------
# Insert at Middle
# ------------------------------------------

numbers.insert(3, 25)

print("\nAfter Inserting 25 at Index 3:")
print(numbers)

# ------------------------------------------
# Insert at End
# ------------------------------------------

numbers.append(50)

print("\nAfter Inserting 50 at End:")
print(numbers)

# ------------------------------------------
# Display Final Array
# ------------------------------------------

print("\nFinal Array:")
print(numbers)
