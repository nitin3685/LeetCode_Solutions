"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        if root.children == None:
            return [root.val]
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend([child for child in node.children])
        return res[::-1]
