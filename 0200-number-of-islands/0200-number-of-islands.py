class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        island = 0
        
        def dfs(grid, i, j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1" and visited[i][j] == False:
                visited[i][j] = True #꼭 필요함!
                dfs(grid, i-1, j)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
                dfs(grid, i, j+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(grid, i, j)
                    island += 1

        return island