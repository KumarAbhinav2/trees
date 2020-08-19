"""
Algo:
current = root
when current is not null
    if current.left does not exists
        visit(current)
        current = current.right
    else:
        #find predecessor
        pred = current.left
        if pred.right and pred.right is not current:
            pred = pred.right
        if pred.right does not exists:
            pred.right = current
            current = current.left
        else:
            pred.right = None
            visit(current)
            current = current.right
"""

class Solution:

    def morrisInOrder(self, root):
        res = []
        curr = root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res