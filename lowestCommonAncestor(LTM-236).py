"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.ans = 0
        def rec(node):
            if not node:
                return False
            # Iterate the left subtree
            left = rec(node.left)
            # Iterate the right subtree
            right = rec(node.right)

            # Check if we found p or q
            mid = node == p or node == q

            # if we found common ancestor, common ancestor could be self node sa well
            if mid+left+right >=2:
                self.ans = node

            return mid or left or right

        rec(root)
        return self.ans

    # Time Complexity: O(n), n is the number of nodes in binary tree
    # Space Complexity: O(n) recursion stack might acquire n space

    def lowestCommonAncestor_iterative(self, root, p, q):
        stack = [root]
        # a dict to hold parent of each node
        parents = {root:None}

        # We iterate till we found either p or q as parents
        while p not in parents or q not in parents:
            node = stack.pop()

            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()
        # update all the ancestors of p
        while p:
            ancestors.add(p)
            p = parents[p]
        # iterate till we find common ancestor of both p and q
        while q not in ancestors:
            q = parents[q]
        return q


    # Time Complexity: O(n), n is number of nodes in binary tree
    # Space Complexity: O(n), ancestor set and dictionary might acquire n spaces in worst case