# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root
        
        # 반복 구조로 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left #젤 왼쪽 leaf node로 내려감
            
            node = stack.pop() # parent로 하나씩 올라가는 것
            
            result = min(result, node.val-prev)
            prev = node.val
            
            node = node.right
        
        return result