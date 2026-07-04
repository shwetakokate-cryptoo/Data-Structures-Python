==========================================
Linked List - Insert Operations
==========================================

This program demonstrates different insertion
operations in a Singly Linked List.

Operations:
- Insert at Beginning
- Insert at End
- Insert at Position
- Display List
"""

from typing import Optional


class Node:
    """Represents a node in the linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Implementation of insertion operations."""

    def __init__(self):
        self.head: Optional[Node] = None

    # --------------------------------------
    # Insert at Beginning
    # --------------------------------------

    def insert_at_beginning(self, data: int) -> None:

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # --------------------------------------
    # Insert at End
    # --------------------------------------

    def insert_at_end(self, data: int) -> None:

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # --------------------------------------
    # Insert at Specific Position
    # --------------------------------------

    def insert_at_position(self, position: int, data: int) -> None:

        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

    # --------------------------------------
    # Display Linked List
    # --------------------------------------

    def display(self) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        print("\nLinked List:")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    linked_list.insert_at_beginning(10)

    linked_list.insert_at_position(3, 25)

    linked_list.display()


if __name__ == "__main__":
    main()


#Expected Output


Linked List:
10 -> 20 -> 25 -> 30 -> 40 -> None
