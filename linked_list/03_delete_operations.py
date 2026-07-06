"""
==========================================
Linked List - Delete Operations
==========================================

This program demonstrates different deletion
operations in a Singly Linked List.

Operations:
- Delete from Beginning
- Delete from End
- Delete by Value
- Display List
"""

from typing import Optional


class Node:
    """Represents a node in the linked list."""

    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    """Implementation of deletion operations."""

    def __init__(self):
        self.head: Optional[Node] = None

    # --------------------------------------
    # Insert at End (Helper Method)
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
    # Delete from Beginning
    # --------------------------------------

    def delete_from_beginning(self) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        deleted = self.head.data
        self.head = self.head.next

        print(f"{deleted} deleted from beginning.")

    # --------------------------------------
    # Delete from End
    # --------------------------------------

    def delete_from_end(self) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(f"{deleted} deleted from end.")
            return

        current = self.head

        while current.next.next:
            current = current.next

        deleted = current.next.data
        current.next = None

        print(f"{deleted} deleted from end.")

    # --------------------------------------
    # Delete by Value
    # --------------------------------------

    def delete_by_value(self, value: int) -> None:

        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print(f"{value} deleted.")
            return

        current = self.head

        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print(f"{value} not found.")
            return

        current.next = current.next.next

        print(f"{value} deleted.")

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

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    linked_list.display()

    print()

    linked_list.delete_from_beginning()
    linked_list.display()

    print()

    linked_list.delete_from_end()
    linked_list.display()

    print()

    linked_list.delete_by_value(30)
    linked_list.display()


if __name__ == "__main__":
    main()

#  Expected Output
Linked List:
10 -> 20 -> 30 -> 40 -> 50 -> None

10 deleted from beginning.

Linked List:
20 -> 30 -> 40 -> 50 -> None

50 deleted from end.

Linked List:
20 -> 30 -> 40 -> None

30 deleted.

Linked List:
20 -> 40 -> None
