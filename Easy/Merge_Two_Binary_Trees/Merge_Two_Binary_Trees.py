# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t1_ptr = t1
        t2_ptr = t2
        t3_ptr = None

        if t1_ptr and t2_ptr:
            t3_ptr = TreeNode(t1_ptr.val + t2_ptr.val)
            t3_ptr.left = self.mergeTrees(t1_ptr.left , t2_ptr.left)
            t3_ptr.right = self.mergeTrees(t1_ptr.right , t2_ptr.right)
        elif t1_ptr:
            t3_ptr = t1_ptr
        else:
            t3_ptr = t2_ptr
        return t3_ptr
