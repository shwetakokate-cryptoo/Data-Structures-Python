"""
==========================================
Linked List - Reverse Linked List
==========================================

This program demonstrates how to reverse
a Singly Linked List.

Operations:
- Insert at End
- Reverse Linked List
- Display List
"""

from typing import Optional


class Node:
    """Represents a node in the linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Implementation of reverse linked list."""

    def __init__(self):
        self.head: Optional[Node] = None

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
    # Reverse Linked List
    # --------------------------------------

    def reverse(self) -> None:

        previous = None
        current = self.head

        while current:

            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    # --------------------------------------
    # Display Linked List
    # --------------------------------------

    def display(self) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse()

    print("\nReversed Linked List:")
    linked_list.display()


if __name__ == "__main__":
    main()
