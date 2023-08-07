class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [[False for _ in range(len(isConnected))] for _ in range(len(isConnected[0]))]
        
        
        def dfs(i,j):
            if i<0 or i>=len(isConnected) or j<0 or j>=len(isConnected[0]) or visited[i][j] == True:
                return
            if isConnected[i][j] == 0:
                return
            visited[i][j] = True
            visited[j][i] = True
            
            for y in range(len(isConnected[0])): #그 행에서 연결된 다음 노드로 넘어가기
                if isConnected[i][y] == 1 and visited[i][y] == False:
                    dfs(y,i)
        
        provinces = 0    
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and visited[i][j] == False:
                    dfs(i,j)
                    provinces += 1
                    
        return provinces