class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp list 만들고 각 index까지 increasing subsequence 길이 적기
        # 지금 수보다 작은 숫자에다가 +1하기
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for prev in range(i-1,-1,-1):
                #print(prev,i,nums[prev],nums[i])
                if nums[prev]<nums[i] and dp[prev]>=dp[i]:
                    dp[i] = dp[prev]+1
                    #print(dp)       
        return max(dp)