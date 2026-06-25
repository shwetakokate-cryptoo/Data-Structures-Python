# ==========================================
# Stack Basics in Python
# ==========================================

# A Stack follows the LIFO principle:
# Last In, First Out

# ------------------------------------------
# Create Stack
# ------------------------------------------

stack = []

# ------------------------------------------
# Push Operation
# ------------------------------------------

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after Push Operations:")
print(stack)

# ------------------------------------------
# Peek Operation
# ------------------------------------------

if stack:
    print("\nTop Element:", stack[-1])

# ------------------------------------------
# Pop Operation
# ------------------------------------------

removed_element = stack.pop()

print("\nPopped Element:", removed_element)

# ------------------------------------------
# Final Stack
# ------------------------------------------

print("\nStack after Pop:")
print(stack)
