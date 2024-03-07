class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for _ in range(len(triangle))]
        dp[0] = triangle[0][0]
        
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                print(i,j)
                if j==0:
                    # 가장자리
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1], triangle[i-1][j])
            #print(triangle)
        return min(triangle[-1])