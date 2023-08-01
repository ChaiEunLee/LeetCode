# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root:
            level = [root]
            while level:
                ans += 1
                level = [kid for node in level for kid in (node.right, node.left) if kid]
                
        return ans
        