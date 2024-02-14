# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # subtree가 다 작고, 커야함
        if not root:
            return
        stack = []
        pre = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val<=pre.val:
                return False
            pre = root
            root = root.right
            
        return True