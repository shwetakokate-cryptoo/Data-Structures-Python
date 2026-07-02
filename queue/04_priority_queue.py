# ==========================================
# Priority Queue Implementation in Python
# ==========================================

# A Priority Queue removes elements based
# on their priority instead of insertion order.

# ------------------------------------------
# Priority Queue Class
# ------------------------------------------

class PriorityQueue:

    def __init__(self):

        self.queue = []

    # --------------------------------------
    # Check if Queue is Empty
    # --------------------------------------

    def is_empty(self):

        return len(self.queue) == 0

    # --------------------------------------
    # Enqueue Operation
    # --------------------------------------

    def enqueue(self, item, priority):

        self.queue.append((priority, item))

        # Sort in descending order of priority
        self.queue.sort(reverse=True)

        print(f"{item} added with priority {priority}.")

    # --------------------------------------
    # Dequeue Operation
    # --------------------------------------

    def dequeue(self):

        if self.is_empty():
            print("Priority Queue is empty.")
            return

        priority, item = self.queue.pop(0)

        print(
            f"Removed: {item} (Priority: {priority})"
        )

    # --------------------------------------
    # Peek Operation
    # --------------------------------------

    def peek(self):

        if self.is_empty():
            print("Priority Queue is empty.")
            return

        priority, item = self.queue[0]

        print(
            f"Next Item: {item} (Priority: {priority})"
        )

    # --------------------------------------
    # Display Queue
    # --------------------------------------

    def display(self):

        if self.is_empty():
            print("Priority Queue is empty.")
            return

        print("\nCurrent Priority Queue:")

        for priority, item in self.queue:
            print(f"{item} (Priority: {priority})")


# ------------------------------------------
# Main Program
# ------------------------------------------

queue = PriorityQueue()

queue.enqueue("Task A", 2)
queue.enqueue("Task B", 5)
queue.enqueue("Task C", 1)
queue.enqueue("Task D", 4)

queue.display()

print()

queue.peek()

print()

queue.dequeue()

queue.display()

#Expected Output


Task A added with priority 2.
Task B added with priority 5.
Task C added with priority 1.
Task D added with priority 4.

Current Priority Queue:
Task B (Priority: 5)
Task D (Priority: 4)
Task A (Priority: 2)
Task C (Priority: 1)

Next Item: Task B (Priority: 5)

Removed: Task B (Priority: 5)

Current Priority Queue:
Task D (Priority: 4)
Task A (Priority: 2)
Task C (Priority: 1)
