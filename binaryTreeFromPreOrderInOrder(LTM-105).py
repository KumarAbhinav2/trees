
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder, inorder) -> TreeNode:
        if not inorder: return

        r = preorder.pop(0)
        root = TreeNode(r)
        m = inorder.index(r)

        root.right = self.buildTree(preorder, inorder[m + 1:])
        root.left = self.buildTree(preorder, inorder[:m])

        return root

    def buildTree2(self, preorder, inorder) -> TreeNode:
        index_map = {num: i for i, num in enumerate(inorder)}

        def rec(l, r):
            if l > r:
                return

            val = preorder.pop(0)
            root = TreeNode(val)
            m = index_map[root.val]
            root.left = rec(l, m - 1)
            root.right = rec(m + 1, r)
            return root

        return rec(0, len(inorder) - 1)



obj = Solution()
obj.buildTree([3,9,20,15,7], [9,3,15,20,7])