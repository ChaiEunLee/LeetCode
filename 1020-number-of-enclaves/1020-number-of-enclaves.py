class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #0:sea, 1:land
        
        # 가장자리에서 출발해서 가장자리와 연결된 땅들은 다 0으로 만들고
        # 그 다음에 남는 1들을 세는 방식?
        # 130.에서 착안한 아이디어
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or visited[i][j]==True:
                return
            visited[i][j] = True
            if grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            
        for i in [0,len(grid)-1]:
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    dfs(i,j)

        for j in [0,len(grid[0])-1]:
            for i in range(len(grid)):
                if grid[i][j] == 1 and visited[i][j] == False:
                    dfs(i,j)
                    
        enclaves = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visited[i][j] == False:
                    enclaves += 1
                    
        return enclaves