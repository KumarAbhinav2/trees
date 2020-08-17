"""
Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedListToBST(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        def rec(arr, start, end):
            if not arr: return None
            if start <= end:
                mid = (start+end)//2
                node = TreeNode(arr[mid])
                node.left = rec(arr, start, mid-1)
                node.right = rec(arr, mid+1, end)
                return node
            return rec(arr, 0, len(arr)-1)