"""
Given a binary tree, return the inorder traversal of its nodes' values.

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""

class Solution:

    def inorderTraversal1(self, root):
        if root is None:return []
        else:
            return self.inorderTraversal1(root.left)+[root.val]+self.inorderTraversal1(root.right)

    def inorderTraversal2(self, root):
        stack = []
        res = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                break
        return res