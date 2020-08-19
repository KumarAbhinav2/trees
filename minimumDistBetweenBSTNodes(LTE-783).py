"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between
the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2,
also between node 3 and node 2.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDiffInBST1(self, root: TreeNode) -> int:
        # morris inorder traversal
        res = []
        curr = root
        min_val = float('inf')
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right
        return min(abs(res[i+1]-res[i]) for i in range(len(res)-1))

    def minDiffInBST2(self, root: TreeNode) -> int:
        if not root:
            return None
        res = []
        self.inorder(root, res)
        return min(res[i + 1] - res[i] for i in range(len(res) - 1))

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)