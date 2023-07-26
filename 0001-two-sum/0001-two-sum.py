class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in myDict:
                return [i, myDict[complement]]
            myDict[nums[i]] = i        