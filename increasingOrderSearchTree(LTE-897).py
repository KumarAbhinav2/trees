"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
the root of the tree, and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def increasingBST(self, root):

        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)

        # we can take it as head node
        ans = cur = TreeNode(None)
        # need not stop after getting the inorder traversal
        # we need to create another tree as per the question
        for val in inorder(root):
            cur.right = TreeNode(val)
            cur = cur.right
        return ans.right


    def increasingBST2(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for val in inorder(root):
            cur.right = TreeNode(val)
            cur = cur.right
        return ans.right