class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # multi dp, uniquepath
        
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        # down, right로만 갈 수 있음
        # 이동할때마다 이전값을 그대로 가져옴. 마지막에 dp[len(obastacle)-1][len(obastacle[0])-1]에서 합산하기 
        dp[0][0] = 1-obstacleGrid[0][0]
        
        for i in range(1,r):
            dp[i][0] = dp[i-1][0] * (1-obstacleGrid[i][0])
        for j in range(1,c):
            dp[0][j] = dp[0][j-1] * (1-obstacleGrid[0][j])
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1-obstacleGrid[i][j])
        return dp[-1][-1]    
        