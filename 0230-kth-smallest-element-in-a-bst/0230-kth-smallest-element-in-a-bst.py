# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth Smallest
        # leftmost로 내려갔다가 올라오면서 right 들르면서 root.left -> root -> root.right 순서로 k번 올라오기
        if not root:
            return
        stack = []
        order = 0
        pre = None
        
        while root or stack:
            while root:
                stack.append(root)
                root=root.left

            root = stack.pop()
            order += 1
            if order==k:
                return root.val
            pre = root
            root = root.right
