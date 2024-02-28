class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        targetvalue = target
        minlength = len(nums)+1
        
        for right in range(len(nums)):
            targetvalue -= nums[right]
            while targetvalue <= 0:
                minlength = min(minlength, right-left+1)
                targetvalue += nums[left]
                left += 1
                #print(left, right, targetvalue) 
            #print(minlength, targetvalue)
        return minlength if minlength<(len(nums)+1) else 0