from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        self.islandmax = 0
        
        def dfs(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1 and visited[i][j] == False:
                self.island += 1
                visited[i][j] = True
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.island = 0
                if grid[i][j] == 1 and visited[i][j] == False:
                    dfs(i,j)
                if self.islandmax < self.island:
                    self.islandmax = self.island
            
        return self.islandmax