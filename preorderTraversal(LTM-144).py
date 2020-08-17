"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""

class Solution:

    def preorderTraversal_recursive(self, root):
        if not root: return []
        else:
            return [root.val]+self.preorderTraversal_recursive(root.left)+self.preorderTraversal_recursive(root.right)

    def preorderTraversal_iterative(self, root):
        if not root: return []
        res = []
        _stack = [root]
        while _stack:
            node = _stack.pop()
            if node:
                res.append(node.val)
                _stack.append(node.right)
                _stack.append(node.left)
        return res