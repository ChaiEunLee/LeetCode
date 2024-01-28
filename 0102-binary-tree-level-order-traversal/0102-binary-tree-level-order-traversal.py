# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root:
            level = [root]
            answer = [[root.val]]
            while level:
                level = [kid for node in level for kid in (node.left, node.right) if kid]
                levelval = []
                for node in level:
                    levelval.append(node.val)
                if levelval:
                    answer.append(levelval)
        return answer