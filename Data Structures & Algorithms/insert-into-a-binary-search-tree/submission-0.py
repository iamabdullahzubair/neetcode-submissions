# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            node = TreeNode(val)
            return node
        
        def dfs(root, val):
            if not root:
                return
            if root.val > val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                dfs(root.left, val)
            else :
                if not root.right:
                    root.right = TreeNode(val)
                    return
                dfs(root.right, val)
        
        dfs(root, val)
        return root
        