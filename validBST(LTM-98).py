"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class Solution:

    def isValidBST_iterative(self, root):
        if not root: return True
        _stack = [(root, -float('inf'), float('inf'))]
        while _stack:
            node, l, r = _stack.pop()
            if node.val <= l or node.val >= r: return False
            if node.left_child: _stack.append((node.left_child, l, node.val))
            if node.right_child: _stack.append((node.right_child, node.val, r))
        return True

    def isValidBST_recursive(self, root):
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left_child, left, node.val) and rec(node.right_child, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf') )
