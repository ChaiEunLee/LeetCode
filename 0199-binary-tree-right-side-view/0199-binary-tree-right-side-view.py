# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level 만들고 -1 return
        answer = []
        if root:
            level = [root]
            while level:
                vals = [node.val for node in level]
                answer.append(vals[-1])
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return answer