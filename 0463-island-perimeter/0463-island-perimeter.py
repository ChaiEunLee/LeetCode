class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    #섬이 있으면 +0 물이 있으면 +1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1: #if island
                    
                    for nx,ny in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                        if nx >= 0 and nx < len(grid) and ny >=0 and ny < len(grid[0]):
                            if grid[nx][ny] == 0:
                                ans += 1
                        else:
                            ans += 1
        return ans                