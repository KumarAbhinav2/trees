"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value
does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion,
as long as the tree remains a BST after insertion. You can return any of them.

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
"""

class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        # If root found none, return newly created Node
        if not root: return TreeNode(val)
        # cheking if the value belongs to left subtree or right subtree
        if val < root.val:
            # recursively call method with reference to left sub tree
            # no need to check if left child exists or not as this will handled in base case
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # Time Complexity: O(H), where H is the height of the Tree
    # Space Complexity: O(n), For maintaining recursive stack

    def insertInyoBST_Iterative(self, root, val):
        node = root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
        return TreeNode(val)

    # Time Complexity: O(H)
    # Space Complexity: O(1)