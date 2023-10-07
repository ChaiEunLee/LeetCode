class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_uniq = list(set(nums))
        nums[0:len(nums_uniq)] = sorted(nums_uniq)
        return len(nums_uniq)