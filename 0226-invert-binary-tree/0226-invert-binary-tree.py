# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # invert하는 함수 만들기
        # 밑에서부터 left, right swap
        
        # base case
        if not root:
            return
        
        if root and root.left and root.right:
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root and root.left:
            self.invertTree(root.left)
        elif root and root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left        
        return root
        
        