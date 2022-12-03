#!/usr/bin/env python3
"""
Riccardo M. Pesce, 2022
"""
from typing import Any, Union

from binary_tree import BinaryTree


class ThreadedBinaryTree(BinaryTree):
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed from other trees
    rather than always creating a new tree in the insert_left or insert_right
    """

    def __init__(self, key: Any) -> None:
        """Create new tree"""
        super().__init__(key)
        self._left_child: Union["ThreadedBinaryTree", None] = None
        self._right_child: Union["ThreadedBinaryTree", None] = None
        self._successor: Union["ThreadedBinaryTree", None] = None

    def get_successor(self) -> Union["ThreadedBinaryTree", None]:
        """Get successor"""
        return self._successor

    def set_successor(self, node) -> None:
        """Set successor"""
        self._successor = node

    successor = property(get_successor, set_successor)

    def insert_left(self, new_node: Any) -> None:
        """Insert left subtree"""
        if isinstance(new_node, ThreadedBinaryTree):
            new_subtree = new_node
        else:
            new_subtree = ThreadedBinaryTree(new_node)

        if self._left_child:
            new_subtree.set_left_child(self._left_child)

        self._left_child = new_subtree

        new_subtree._successor = new_subtree.find_successor()

    def insert_right(self, new_node: Any) -> None:
        """Insert right subtree"""
        if isinstance(new_node, ThreadedBinaryTree):
            new_subtree = new_node
        else:
            new_subtree = ThreadedBinaryTree(new_node)

        if self._right_child:
            new_subtree.set_right_child(self._right_child)
        self._right_child = new_subtree

        new_subtree._successor = new_subtree.find_successor()

    def inorder(self) -> None:
        """In-order tree traversal"""
        cur = self.find_min()
        while cur:
            print(cur.key)
            cur = cur.find_successor()


if __name__ == "__main__":
    t = BinaryTree("/")
    t.insert_left(7)
    t.insert_right(0)
    t.preorder()

