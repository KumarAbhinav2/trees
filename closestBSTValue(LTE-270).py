"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""

class Solution:
    def closestValue(self, root, target):
        if not root: return
        pred = float('-inf')

        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        ordered = inorder(root)

        for i in range(len(ordered)):
            if pred <= target and ordered[i] > target:
                return min(pred, ordered[i], key=lambda x: abs(target - x))
            pred = ordered[i]
        return pred

    # Time Complexity: O(H)
    # Space Complexity: O(H)


    def closestValue_better(self, root, target):
        stack = []
        pred = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if pred <=target and target>root.val:
                return min(pred, root.val, key = lambda x: abs(target-x))

            pred = root.val
            root = root.right

        return pred

    # Time Complexity: O(k), till you found closest i.e index of the closest element
    # Space Complexity: O(H), we have extra stack


    def closestValue_better1(self, root, target):
        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: abs(target-x))
            root = root.left if target < root.val else root.right
        return closest

    # Time Complexity: O(H), can't be O(logN) as tree might not be actually balanced 
    # Space Complexity: O(1)