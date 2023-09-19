# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root):
        view = []
        if root:
            level = [root]
            while level:
                #level에 순서대로 넣으니까 가장 오른쪽에 있는 node값을 view에 넣는다.
                view += level[-1].val,
                #각 level에 있는 노드별로 left, right가 있으면 그걸 level로 업데이트. 
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view