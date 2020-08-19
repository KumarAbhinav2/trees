"""
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes,
then this node's value is the smaller value among its two sub-nodes. More formally,
the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes'
value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findSecondMinimumValue(self, root) -> int:
        def minimum(root):
            mini = float('inf')
            if root.right and root.right.val!=root.val:
                mini = min(mini,root.right.val)
            if root.left and root.left.val!=root.val:
                mini = min(mini,root.left.val)
            if root.right:
                mini =  min(mini,minimum(root.right))
            if root.left:
                mini =  min(mini, minimum(root.left))
            return mini

        res = minimum(root)
        if res==float('inf'):
            return -1
        return res

    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        def rec(root):
            if not root: return []
            else:
                return rec(root.left)+[root.val]+rec(root.right)
        res = set(rec(root))
        if len(res)>=2:
            return sorted(list(res))[1]
        else:
            return -1
