class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)
        if len(numsset)<len(nums):
            return True
        return False