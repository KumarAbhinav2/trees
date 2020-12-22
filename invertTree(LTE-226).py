"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class Solution:
    def invertTree(self, root):
        if not root: return
        # recursive calls till reaches leaf nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        # swap the childs
        root.left, root.right = root.right, root.left
        return root

    # Time complexity: O(h) , h is the height of the tree
    # Space complexity: O(N)

    def invertTree_Iterative(self, root):
        if not root: return
        _stack = [root]
        while _stack:
            node = _stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                _stack+=node.left, node.right
        return root
    # Time Complexity: O(N), all the element once added to stack
    # Space Complexity: O(N) for the stack

