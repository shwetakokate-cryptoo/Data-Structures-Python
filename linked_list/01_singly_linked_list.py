"""
==========================================
Singly Linked List Implementation
==========================================

This program demonstrates the basic implementation
of a Singly Linked List in Python.

Operations:
- Insert at End
- Display List
"""

from typing import Optional


class Node:
    """Represents a single node in a linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Implementation of a Singly Linked List."""

    def __init__(self):
        self.head: Optional[Node] = None

    def insert(self, data: int) -> None:
        """Insert a node at the end of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self) -> None:
        """Display all elements of the linked list."""

        if self.head is None:
            print("Linked List is empty.")
            return

        current = self.head

        print("\nLinked List:")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def main() -> None:
    """Main function."""

    linked_list = SinglyLinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)

    linked_list.display()


if __name__ == "__main__":
    main()

# Expected Output

Linked List:
10 -> 20 -> 30 -> 40 -> None
