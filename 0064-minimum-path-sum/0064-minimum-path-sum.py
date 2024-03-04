class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # top left -> bottom right sum 
        # multi dp
        dp = grid.copy()
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                if i==0 and j==0:
                    continue
                if i>0 and j>0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i==0:
                    dp[i][j] += dp[i][j-1]
                elif j==0:
                    dp[i][j] += dp[i-1][j]
                #print(dp)
        return dp[len(dp)-1][len(dp[0])-1]