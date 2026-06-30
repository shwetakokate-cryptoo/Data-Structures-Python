# ==========================================
# Queue Implementation Using Class in Python
# ==========================================

# A Queue follows the FIFO (First In, First Out)
# principle. This implementation uses a class.

# ------------------------------------------
# Queue Class
# ------------------------------------------

class Queue:

    def __init__(self):
        self.items = []

    # Enqueue Operation
    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} added to the queue.")

    # Dequeue Operation
    def dequeue(self):

        if self.is_empty():
            return "Queue is empty."

        return self.items.pop(0)

    # Peek Operation
    def peek(self):

        if self.is_empty():
            return "Queue is empty."

        return self.items[0]

    # Check if Queue is Empty
    def is_empty(self):
        return len(self.items) == 0

    # Display Queue
    def display(self):

        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.items)


# ------------------------------------------
# Main Program
# ------------------------------------------

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

print("\nFront Element:", queue.peek())

print("\nDequeued Element:", queue.dequeue())

queue.display()

#Expected Output

10 added to the queue.
20 added to the queue.
30 added to the queue.
Current Queue: [10, 20, 30]

Front Element: 10

Dequeued Element: 10
Current Queue: [20, 30]
