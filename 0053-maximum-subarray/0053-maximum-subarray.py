class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -10000
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            #print(best_sum, current_sum)
            best_sum = max(best_sum, current_sum)
        return best_sum