"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
"""

class Solution:

    def height(self, root):
        if not root:
            return 0
        return 1+max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if not root:
            return -1
        return abs(self.height(root.left) - self.height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)

    def isBalancedHelper(self, root) -> bool:
        if not root: return True, -1

        leftBalanced, left_h = self.isBalancedHelper(root.left)
        if not leftBalanced:
            return False, 0
        rightBalanced, right_h = self.isBalancedHelper(root.right)
        if not rightBalanced:
            return False, 0

        return abs(left_h - right_h) < 2, 1 + max(left_h, right_h)

    def isBalanced_bu(self, root):
        return self.isBalancedHelper(root)[0]

    # Time Complexity: O(n)
    # Space Compelxity: O(n)