class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root
