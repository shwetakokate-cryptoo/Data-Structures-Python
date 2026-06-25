# ==========================================
# Array Update in Python
# ==========================================

# This program demonstrates how to
# update elements in an array using indexes.

# ------------------------------------------
# Initial Array
# ------------------------------------------

numbers = [10, 20, 30, 40, 50]

print("Original Array:")
print(numbers)

# ------------------------------------------
# Update Element
# ------------------------------------------

index = int(input("\nEnter index to update: "))

if 0 <= index < len(numbers):

    new_value = int(
        input("Enter new value: ")
    )

    numbers[index] = new_value

    print("\nArray Updated Successfully!")

else:
    print("\nInvalid Index!")

# ------------------------------------------
# Display Updated Array
# ------------------------------------------

print("\nUpdated Array:")
print(numbers)
