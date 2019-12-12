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
        res = []
        for index in range(len(root.children)):
            res += self.postorder(root.children[index])
        res += [root.val]
        return res
        
