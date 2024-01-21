# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 누 노드 사이 가장 긴 path 길이
        def dfs(node):
            if not node:
                return -1
            
            # 왼쪽, 오른쪽의 각 리트 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left+right+2)
            # 상태값
            return max(left,right) + 1
        
        dfs(root)
        return self.longest