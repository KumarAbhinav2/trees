"""
Condition for Binary search tree:
NodeValues(leftsubtree) <= CurrentNodeValue < NodeValues(rightsubtree)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left_child  = None
        self.right_child = None


class BST:
    """Binary search tree"""
    def __init__(self):
        self.root = None

    def insert_node(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:                       # need to traverse left sub tree
            if node.left_child:
                self._insert(node.left_child, val)
            else:
                node.left_child = Node(val)      # absence  of left sub tree
        else:
            if node.right_child:
                self._insert(node.right_child, val)
            else:
                node.right_child = Node(val)


