"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree1(self, inorder, postorder) -> TreeNode:
        index_map = { num:i for i, num in enumerate(inorder) }   # do that index search will be faster
        def rec(left, right):
            if left > right: return
            root = TreeNode(postorder.pop())
            mid = index_map[ root.val ]
            root.right = rec(mid+1, right)      # reverse order - first iterate right tree
            root.left = rec(left, mid-1)
            return root
        return rec(0, len(inorder)-1)

    def buildTree_recursive(self, inorder, postorder) -> TreeNode:
        if not inorder:
            return
        r = postorder.pop()
        node = TreeNode(r)
        i = inorder.index(r)

        node.right = self.buildTree_recursive(inorder[i + 1:], postorder)
        node.left = self.buildTree_recursive(inorder[:i], postorder)
        return node


obj = Solution()
obj.buildTree1([9,3,15,20,7], [9,15,7,20,3])
obj.buildTree_recursive([9,3,15,20,7], [9,15,7,20,3])
