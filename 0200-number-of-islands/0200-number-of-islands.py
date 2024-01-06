class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return False
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(x,y):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and visited[x][y] == False and grid[x][y] == '1':
                visited[x][y] = True
                for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    dfs(nx,ny)

                    
        numisland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] is False and grid[i][j] == '1':
                    dfs(i,j)
                    numisland += 1

        return numisland