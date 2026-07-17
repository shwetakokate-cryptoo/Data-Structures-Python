"""
==========================================
Binary Tree Basics
==========================================

This program demonstrates the basic
implementation of a Binary Tree.

Operations:
- Create Nodes
- Build Binary Tree
- Preorder Traversal
"""

from typing import Optional


class TreeNode:
    """Represents a node in a Binary Tree."""

    def __init__(self, data: int):
        self.data = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinaryTree:
    """Binary Tree implementation."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    # --------------------------------------
    # Preorder Traversal
    # --------------------------------------

    def preorder(self, node: Optional[TreeNode]) -> None:
        """
        Traverse the tree in Preorder.
        Root -> Left -> Right
        """

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)
        self.preorder(node.right)


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    tree = BinaryTree()

    # Create Nodes
    tree.root = TreeNode(10)

    tree.root.left = TreeNode(20)
    tree.root.right = TreeNode(30)

    tree.root.left.left = TreeNode(40)
    tree.root.left.right = TreeNode(50)

    tree.root.right.right = TreeNode(60)

    print("Binary Tree (Preorder Traversal):")

    tree.preorder(tree.root)

    print()


if __name__ == "__main__":
    main()

"""Expected Output
Binary Tree (Preorder Traversal):
10 20 40 50 30 60"""
