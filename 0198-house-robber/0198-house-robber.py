class Solution:
    def rob(self, nums: List[int]) -> int:
        # no adjacent houses
        # maximum amount of money
        # 각 index 별로 이전 집들 중에서 가장 많이 훔칠수 있는 값을 저장하기 
        dp = collections.defaultdict(int)
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        
        dp[0] = nums[0] 
        dp[1] = nums[1]
        dp[2] = nums[2] + dp[0]

        for i in range(2,len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3]) #i-1은 불가, i-4는 i-2에 포함되어있으니까. 

        return max(dp.values())
    