"""
==========================================
Binary Search Tree - Delete Node
==========================================

This program demonstrates deleting nodes
from a Binary Search Tree.

Operations:
- Insert Node
- Delete Node
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
        self.root = self._insert(self.root, data)

    def _insert(
        self,
        node: Optional[TreeNode],
        data: int
    ) -> TreeNode:

        if node is None:
            return TreeNode(data)

        if data < node.data:
            node.left = self._insert(node.left, data)

        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    # --------------------------------------
    # Delete Node
    # --------------------------------------

    def delete(self, data: int) -> None:
        self.root = self._delete(self.root, data)

    def _delete(
        self,
        node: Optional[TreeNode],
        data: int
    ) -> Optional[TreeNode]:

        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)

        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:

            # Case 1: No left child
            if node.left is None:
                return node.right

            # Case 2: No right child
            if node.right is None:
                return node.left

            # Case 3: Two children
            successor = self._min_value_node(node.right)

            node.data = successor.data

            node.right = self._delete(
                node.right,
                successor.data
            )

        return node

    # --------------------------------------
    # Find Minimum Node
    # --------------------------------------

    def _min_value_node(
        self,
        node: TreeNode
    ) -> TreeNode:

        current = node

        while current.left:
            current = current.left

        return current

    # --------------------------------------
    # Inorder Traversal
    # --------------------------------------

    def inorder(
        self,
        node: Optional[TreeNode]
    ) -> None:

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

    print("Original BST:")
    bst.inorder(bst.root)

    print("\n")

    print("Deleting 70...\n")

    bst.delete(70)

    print("BST After Deletion:")
    bst.inorder(bst.root)

    print()


if __name__ == "__main__":
    main()
