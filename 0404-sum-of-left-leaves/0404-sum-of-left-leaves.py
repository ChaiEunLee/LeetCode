# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, False)]), 0 #(root, False) 소괄호로 감싸야함.        
        while q:
            cur, isleft = q.popleft()
            if not cur.left and not cur.right and isleft: #left, right도 없고 그 노드가 leftnode일 때 
                ans += cur.val
            if cur.right: 
                q.append((cur.right, False)) #right가 있으면 일단 내려가야해서 False로 q에 넣기
            if cur.left:
                q.append((cur.left, True)) #left가 있으면 True로 넣어서 ans에 add하려고. 
        return ans