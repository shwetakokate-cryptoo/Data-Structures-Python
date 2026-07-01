# ==========================================
# Circular Queue Implementation in Python
# ==========================================

# A Circular Queue efficiently utilizes
# memory by reusing empty spaces.

# ------------------------------------------
# Circular Queue Class
# ------------------------------------------

class CircularQueue:

    def __init__(self, size):

        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # --------------------------------------
    # Check if Queue is Empty
    # --------------------------------------

    def is_empty(self):

        return self.front == -1

    # --------------------------------------
    # Check if Queue is Full
    # --------------------------------------

    def is_full(self):

        return (self.rear + 1) % self.size == self.front

    # --------------------------------------
    # Enqueue Operation
    # --------------------------------------

    def enqueue(self, item):

        if self.is_full():
            print("Queue Overflow!")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = item

        print(f"{item} inserted.")

    # --------------------------------------
    # Dequeue Operation
    # --------------------------------------

    def dequeue(self):

        if self.is_empty():
            print("Queue Underflow!")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:

            self.front = -1
            self.rear = -1

        else:

            self.front = (self.front + 1) % self.size

        print(f"{removed} removed.")

    # --------------------------------------
    # Display Queue
    # --------------------------------------

    def display(self):

        if self.is_empty():
            print("Queue is empty.")
            return

        print("\nCurrent Queue:")

        index = self.front

        while True:

            print(self.queue[index], end=" ")

            if index == self.rear:
                break

            index = (index + 1) % self.size

        print()


# ------------------------------------------
# Main Program
# ------------------------------------------

queue = CircularQueue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.display()

queue.dequeue()

queue.display()

queue.enqueue(50)
queue.enqueue(60)

queue.display()



Expected Output


10 inserted.
20 inserted.
30 inserted.
40 inserted.

Current Queue:
10 20 30 40

10 removed.

Current Queue:
20 30 40

50 inserted.
60 inserted.

Current Queue:
20 30 40 50 60
