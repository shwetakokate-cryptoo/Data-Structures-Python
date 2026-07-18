"""
==========================================
Binary Tree Traversals
==========================================

This program demonstrates the three
Depth-First Search (DFS) traversals
of a Binary Tree.

Traversals:
- Preorder
- Inorder
- Postorder
"""

from typing import Optional


class TreeNode:
    """Represents a node in a Binary Tree."""

    def __init__(self, data: int):
        self.data = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinaryTree:
    """Binary Tree traversal implementation."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    # --------------------------------------
    # Preorder Traversal
    # Root -> Left -> Right
    # --------------------------------------

    def preorder(self, node: Optional[TreeNode]) -> None:

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)
        self.preorder(node.right)

    # --------------------------------------
    # Inorder Traversal
    # Left -> Root -> Right
    # --------------------------------------

    def inorder(self, node: Optional[TreeNode]) -> None:

        if node is None:
            return

        self.inorder(node.left)

        print(node.data, end=" ")

        self.inorder(node.right)

    # --------------------------------------
    # Postorder Traversal
    # Left -> Right -> Root
    # --------------------------------------

    def postorder(self, node: Optional[TreeNode]) -> None:

        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)

        print(node.data, end=" ")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    tree = BinaryTree()

    # Build Binary Tree
    tree.root = TreeNode(10)

    tree.root.left = TreeNode(20)
    tree.root.right = TreeNode(30)

    tree.root.left.left = TreeNode(40)
    tree.root.left.right = TreeNode(50)

    tree.root.right.right = TreeNode(60)

    print("Preorder Traversal:")
    tree.preorder(tree.root)

    print("\n")

    print("Inorder Traversal:")
    tree.inorder(tree.root)

    print("\n")

    print("Postorder Traversal:")
    tree.postorder(tree.root)

    print()


if __name__ == "__main__":
    main()

Expected Output

Preorder Traversal:
10 20 40 50 30 60

Inorder Traversal:
40 20 50 10 30 60

Postorder Traversal:
40 50 20 60 30 10
