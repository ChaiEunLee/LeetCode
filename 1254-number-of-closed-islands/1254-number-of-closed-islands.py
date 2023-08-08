class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 0:island, 1:water
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 0:
                return
            if visited[i][j] == True:
                return
            visited[i][j] = True
            grid[i][j] = 1
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        
        for i in [0, len(grid)-1]:
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and visited[i][j] == False:
                    dfs(i,j)
                    
        for j in [0,len(grid[0])-1]:
            for i in range(len(grid)):
                if grid[i][j] == 0 and visited[i][j] == False:
                    dfs(i,j)
        #print(grid)
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and visited[i][j] == False:
                    dfs(i,j)
                    island += 1

        return island
    