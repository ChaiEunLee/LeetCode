class Solution:
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:

        if n<=1:
            return n
        # 앞에서 계산했던 값이라면 그 값을 기억해놨다가 return 
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
        
        