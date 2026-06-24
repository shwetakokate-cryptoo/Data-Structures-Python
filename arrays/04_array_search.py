# ==========================================
# Array Search in Python
# ==========================================

# This program searches for an element
# in an array using Linear Search.

# ------------------------------------------
# Function to Search Element
# ------------------------------------------

def linear_search(numbers, target):

    for index in range(len(numbers)):

        if numbers[index] == target:
            return index

    return -1


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    numbers = [10, 20, 30, 40, 50]

    print("Array:")
    print(numbers)

    target = int(input("\nEnter element to search: "))

    result = linear_search(numbers, target)

    if result != -1:
        print(
            f"\nElement found at index {result}"
        )
    else:
        print("\nElement not found.")


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
