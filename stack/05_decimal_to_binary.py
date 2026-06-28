# ==========================================
# Decimal to Binary Using Stack
# ==========================================

# This program converts a decimal number
# to its binary representation using a stack.

# ------------------------------------------
# Function to Convert Decimal to Binary
# ------------------------------------------

def decimal_to_binary(number):

    # Handle special case
    if number == 0:
        return "0"

    stack = []

    # Store remainders in the stack
    while number > 0:
        remainder = number % 2
        stack.append(remainder)
        number //= 2

    binary = ""

    # Pop elements to get binary representation
    while stack:
        binary += str(stack.pop())

    return binary


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    print("===================================")
    print("   DECIMAL TO BINARY USING STACK")
    print("===================================")

    try:
        number = int(input("\nEnter a non-negative integer: "))

        if number < 0:
            print("\nPlease enter a non-negative integer.")
            return

        binary = decimal_to_binary(number)

        print(f"\nDecimal Number : {number}")
        print(f"Binary Number  : {binary}")

    except ValueError:
        print("\nInvalid input! Please enter an integer.")


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
