class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = []
        idx = 0
        for i in range(len(nums)):
            if nums[i] not in uniq:
                nums[idx] = nums[i]
                uniq.append(nums[i])
                idx += 1
        return idx