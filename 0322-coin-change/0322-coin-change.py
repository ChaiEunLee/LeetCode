class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # col: amounts, value: counts
        dp = [0] + [float('inf') for i in range(amount)] #[0,inf,inf,...,inf]
        for i in range(1,amount+1): #amount
            for coin in coins: #coin
                if i-coin>=0: #amount-coin>=0 (amount의 part가 될수있다면)
                    dp[i] = min(dp[i], dp[i-coin]+1) #지금 dp[i]랑 이전 coin 개수에서 +1 추가한거랑 비교해서 적은 개수의 값으로 지정
                    #print(dp)
        if dp[-1] == float('inf'): #마지막 amount가 inf면 없는것.
            return -1 
        return dp[-1]
        