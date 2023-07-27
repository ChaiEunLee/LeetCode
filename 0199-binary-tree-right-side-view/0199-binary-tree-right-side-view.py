# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            level = [root]
            while level:
                ans.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return ans