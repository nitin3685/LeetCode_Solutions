# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        import collections
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
        return res[::-1]
            
