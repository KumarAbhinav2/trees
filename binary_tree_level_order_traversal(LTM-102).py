"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

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

    def levelOrder_dfs1(self, root):
        level = [root]
        res = []
        if not root: return None
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
                level = [node for node in temp if node]
        return res

    def levelOrder_dfs2(self, root):
        if not root: return []
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if len(res) < level+1:
                res.append([])
            res[level].append(curr.val)
            if curr.right:
                stack.append((curr.right, level+1))
            if curr.left:
                stack.append((curr.left, level+1))
        return res

    def levelOrder_dfs3(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                stack.append((curr.right, level+1))
                stack.append((curr.left, level+1))
        return res

    def levelOrder_bfs(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop()
            if curr:
                if len(res) < level+1:
                    res.append([])
                res[level].append(curr.val)
                queue.append((curr.right, level+1))
                queue.append((curr.left, level+1))
        return res