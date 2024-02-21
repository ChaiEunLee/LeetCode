class Solution:
    def climbStairs(self, n: int) -> int:
        # how many distinct ways 
        # step list 만들고 각 step 별로 숫자 카운트
        if n==1:
            return 1
        step = [0]*(n+1)
        step[1] = 1
        step[2] = 1
        for i in range(2,n+1):
            step[i] = step[i]+step[i-1]+step[i-2]
            print(step)
        return step[n]