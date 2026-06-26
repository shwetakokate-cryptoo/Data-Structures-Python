# ==========================================
# Stack Implementation Using Class in Python
# ==========================================

# A Stack follows the LIFO (Last In, First Out)
# principle. This implementation uses a class.

# ------------------------------------------
# Stack Class
# ------------------------------------------

class Stack:

    def __init__(self):
        self.items = []

    # Push Operation
    def push(self, item):
        self.items.append(item)
        print(f"{item} pushed into stack.")

    # Pop Operation
    def pop(self):

        if self.is_empty():
            return "Stack is empty."

        return self.items.pop()

    # Peek Operation
    def peek(self):

        if self.is_empty():
            return "Stack is empty."

        return self.items[-1]

    # Check if Stack is Empty
    def is_empty(self):
        return len(self.items) == 0

    # Display Stack
    def display(self):

        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current Stack:", self.items)


# ------------------------------------------
# Main Program
# ------------------------------------------

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("\nTop Element:", stack.peek())

print("\nPopped Element:", stack.pop())

stack.display()
