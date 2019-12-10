# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        stack = []
        stack.append([t1, t2])
        while len(stack) != 0:
            t = stack.pop()
            if t[1] is None:
                continue
            
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append([t[0].left, t[1].left])
            
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append([t[0].right, t[1].right])
            
        return t1
