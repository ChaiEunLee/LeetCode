class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}
        for n in nums:
            if n in myDict:
                myDict[n] += 1
            else:
                myDict[n] = 1
        
        # list 길이가 1인 경우가 있을수 있어서
        for key, value in myDict.items():
            if value > len(nums)//2:
                return key