# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level의 평균 append
        answer = []
        if root:
            level = [root]
        while level:
            vals = [node.val for node in level]
            answer.append(mean(vals))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return answer