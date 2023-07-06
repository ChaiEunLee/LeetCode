from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        q = deque([])
        
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    
        while q:
            x,y = q.popleft()
            for nx,ny in (x,y-1),(x,y+1),(x-1,y),(x+1,y):
                if nx < 0 or nx == len(grid) or ny < 0 or ny == len(grid[0]) or visited[nx][ny] != 0 or grid[nx][ny] == 0 or grid[nx][ny] == 2:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                #나중에 +1해서 값 구하면 됨. 아니면 0이랑 헷갈려서 
        
        minute = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if visited[x][y] == 0 and grid[x][y] == 1:
                    return -1
                else:
                    minute = max(visited[x][y], minute)
        
        return minute
        