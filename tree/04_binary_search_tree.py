"""
==========================================
Binary Search Tree (BST)
==========================================

This program demonstrates the implementation
of a Binary Search Tree.

Operations:
- Insert Node
- Search Node
- Inorder Traversal
"""

from typing import Optional


class TreeNode:
    """Represents a node in a Binary Search Tree."""

    def __init__(self, data: int):
        self.data = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinarySearchTree:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    # --------------------------------------
    # Insert Node
    # --------------------------------------

    def insert(self, data: int) -> None:
        """Insert a value into the BST."""

        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(
        self,
        node: Optional[TreeNode],
        data: int
    ) -> TreeNode:

        if node is None:
            return TreeNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)

        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)

        return node

    # --------------------------------------
    # Search Node
    # --------------------------------------

    def search(self, data: int) -> bool:
        """Search for a value in the BST."""

        return self._search_recursive(self.root, data)

    def _search_recursive(
        self,
        node: Optional[TreeNode],
        data: int
    ) -> bool:

        if node is None:
            return False

        if node.data == data:
            return True

        if data < node.data:
            return self._search_recursive(node.left, data)

        return self._search_recursive(node.right, data)

    # --------------------------------------
    # Inorder Traversal
    # --------------------------------------

    def inorder(self, node: Optional[TreeNode]) -> None:
        """Display BST in sorted order."""

        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        bst.insert(value)

    print("Inorder Traversal (Sorted):")
    bst.inorder(bst.root)

    print("\n")

    value = 60

    if bst.search(value):
        print(f"{value} found in the BST.")
    else:
        print(f"{value} not found in the BST.")


if __name__ == "__main__":
    main()
