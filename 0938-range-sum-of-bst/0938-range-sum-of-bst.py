# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # high를 만나면 그 기준으로 그것보다 작은 수들의 합산으로 계산하면 될듯
        if root:
            self.rangeSumBST(root.left, low, high)
            if root.val <= high and root.val >= low:
                self.answer += root.val
            self.rangeSumBST(root.right, low, high)
        
        return self.answer