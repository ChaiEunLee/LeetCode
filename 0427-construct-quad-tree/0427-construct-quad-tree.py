"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node(True, True, None, None, None, None)
        # 모든 elements가 한개의 값일 때
        if len(set([item for row in grid for item in row])) == 1:
            root.val = bool(grid[0][0]) # val를 넣는데 굳이 bool로 넣는 이유는??
        else:
            root.isLeaf = False
            size = len(grid)
            root.topLeft = self.construct([row[:size//2] for row in grid[:size//2]])
            root.topRight = self.construct([row[size//2:] for row in grid[:size//2]])
            root.bottomLeft = self.construct([row[:size//2] for row in grid[size//2:]])
            root.bottomRight = self.construct([row[size//2:] for row in grid[size//2:]])
        return root