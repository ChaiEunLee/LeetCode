class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights)==0:
            return
        
        n = len(heights)
        m = len(heights[0])
        
        ans = []
        pacific = [[False for i in range(m)] for j in range(n)]
        atlantic = [[False for i in range(m)] for j in range(n)]
        
        visited = [[False for i in range(m)] for j in range(n)]
        
        def dfs(mat, ispacific, i, j):
            if ispacific:
                visited = pacific
            else:
                visited = atlantic
            
            if visited[i][j]:
                return
            visited[i][j] = True
            
            if pacific[i][j] and atlantic[i][j]:
                ans.append([i,j])
                
            if i+1 < n and mat[i+1][j] >= mat[i][j]:
                dfs(mat, ispacific, i+1, j)
            if i-1 >= 0 and mat[i-1][j] >= mat[i][j]:
                dfs(mat, ispacific, i-1, j)
            if j+1 < m and mat[i][j+1] >= mat[i][j]:
                dfs(mat, ispacific, i, j+1)
            if j-1 >= 0 and mat[i][j-1] >= mat[i][j]:
                dfs(mat, ispacific, i, j-1)                

                
        for i in range(n):
            dfs(heights, True, i, 0) #left
            dfs(heights, False,i,m-1) #right
        for j in range(m):
            dfs(heights, True, 0, j) #up
            dfs(heights, False, n-1, j) #down
            
        return ans
    