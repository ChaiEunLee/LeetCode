# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sumleave = 0
        level = [root]
        
        while level:
            prev, level = level, [kid for node in level for kid in (node.left, node.right) if kid]
        
        for leave in prev:
            sumleave += leave.val
        
        return sumleave