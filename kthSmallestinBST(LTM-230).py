"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.



Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        res = []
        _stack = []
        while _stack or root:
            while root:
                _stack.append(root)
                root = root.left
            root = _stack.pop()
            res.append(root)
            root = root.right
        return res[k-1].val

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        def rec(root):
            if not root:return []
            else:
                return rec(root.left)+[root.val]+rec(root.right)
        res = rec(root)
        return res[k-1]



