# ==========================================
# Balanced Parentheses Checker
# ==========================================

# This program checks whether an expression
# has balanced parentheses using a stack.

# ------------------------------------------
# Function to Check Balance
# ------------------------------------------

def is_balanced(expression):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:

        # Push opening brackets
        if char in "([{":
            stack.append(char)

        # Check closing brackets
        elif char in ")]}":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    print("===================================")
    print(" BALANCED PARENTHESES CHECKER")
    print("===================================")

    expression = input(
        "\nEnter an expression: "
    )

    if is_balanced(expression):
        print("\nResult: Balanced")
    else:
        print("\nResult: Not Balanced")


# ------------------------------------------
# Run Program
# ------------------------------------------

main()
