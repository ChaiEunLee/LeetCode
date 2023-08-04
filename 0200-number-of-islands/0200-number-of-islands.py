class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #base
        if not grid:
            return 0
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        island = 0
        
        def dfs(i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1" and visited[i][j] == False:
                visited[i][j] = True
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(i, j)
                    island += 1

        return island