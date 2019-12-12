"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import defaultdict
        if not root:
            return None
        if not root.children:
            return [[root.val]]
        res_dict = defaultdict(list)
        level = 0
        
        def mylo(node,res_dict,level):
            res_dict[level].extend([node.val])
            level += 1
            for child in node.children:
                mylo(child,res_dict,level)
        mylo(root,res_dict,level)
        return res_dict.values()
