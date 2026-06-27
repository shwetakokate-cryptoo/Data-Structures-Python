# ==========================================
# Reverse a String Using Stack
# ==========================================

# This program reverses a string
# using stack operations.

# ------------------------------------------
# Function to Reverse String
# ------------------------------------------

def reverse_string(text):

    stack = []

    # Push each character onto the stack
    for character in text:
        stack.append(character)

    reversed_text = ""

    # Pop characters from the stack
    while stack:
        reversed_text += stack.pop()

    return reversed_text


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    print("===================================")
    print("   REVERSE STRING USING STACK")
    print("===================================")

    text = input("\nEnter a string: ")

    reversed_text = reverse_string(text)

    print("\nOriginal String :", text)
    print("Reversed String :", reversed_text)


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
