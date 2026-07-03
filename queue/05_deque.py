# ==========================================
# Deque (Double-Ended Queue) in Python
# ==========================================

from collections import deque


class DequeExample:
    """
    Demonstrates basic deque operations using
    Python's collections.deque.
    """

    def __init__(self):
        self.deque = deque()

    # --------------------------------------
    # Insert at Front
    # --------------------------------------

    def insert_front(self, item):
        self.deque.appendleft(item)
        print(f"{item} inserted at the front.")

    # --------------------------------------
    # Insert at Rear
    # --------------------------------------

    def insert_rear(self, item):
        self.deque.append(item)
        print(f"{item} inserted at the rear.")

    # --------------------------------------
    # Delete from Front
    # --------------------------------------

    def delete_front(self):

        if not self.deque:
            print("Deque is empty.")
            return

        removed = self.deque.popleft()
        print(f"{removed} removed from the front.")

    # --------------------------------------
    # Delete from Rear
    # --------------------------------------

    def delete_rear(self):

        if not self.deque:
            print("Deque is empty.")
            return

        removed = self.deque.pop()
        print(f"{removed} removed from the rear.")

    # --------------------------------------
    # Display Deque
    # --------------------------------------

    def display(self):

        if not self.deque:
            print("Deque is empty.")
            return

        print("\nCurrent Deque:")
        print(list(self.deque))


# ------------------------------------------
# Main Program
# ------------------------------------------

dq = DequeExample()

dq.insert_rear(20)
dq.insert_rear(30)
dq.insert_front(10)
dq.insert_front(5)

dq.display()

print()

dq.delete_front()
dq.delete_rear()

dq.display()

#Expected Output

20 inserted at the rear.
30 inserted at the rear.
10 inserted at the front.
5 inserted at the front.

Current Deque:
[5, 10, 20, 30]

5 removed from the front.
30 removed from the rear.

Current Deque:
[10, 20]
