"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
class Solution:
    def levelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop()
            if len(res) < level+1:
                res.append([])
            res[level].append(curr.val)
            queue.append((curr.left, level+1))
            queue.append((curr.right, level+1))
        return res

    def levelOrder_recursive(self, root):
        if not root:
            return None

        def rec(curr, res, level):
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                rec(curr.left, res, level+1)
                rec(curr.right, res, level+1)
            return res
        return rec(root, [], 0)