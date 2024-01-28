# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, level, direction = [], [root], 1
        while level:
            res.append([n.val for n in level][::direction]) #::-1이면 거꾸로
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res