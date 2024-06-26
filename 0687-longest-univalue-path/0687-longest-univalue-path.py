# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # DFS로 내려가다가 leaf에 도달하면 그때부터 backtracking으로 거리를 누적해 계산하는 방식
        def dfs(node):
            if node is None:
                return 0
            
            # 존재하지 않는 노드까지 DFS 재귀 탐색. leaf에 도달하면 0을 return. 
            left = dfs(node.left) 
            right = dfs(node.right)
            
            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            # 왼쪽과 오른쪽 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left+right)
            return max(left, right)
        dfs(root)
        return self.result