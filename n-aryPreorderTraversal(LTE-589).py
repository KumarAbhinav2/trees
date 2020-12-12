"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""

class Solution:

    def preorder(self, root):
        if not root:
            return []

        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children[::-1])
        return output

    # Time Complexity: O(n)
    # Space Complexity: O(n)