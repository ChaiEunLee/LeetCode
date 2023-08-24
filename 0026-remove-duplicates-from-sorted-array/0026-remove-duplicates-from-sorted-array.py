class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqcnt = 0
        for i in range(len(nums)):
            if nums[i] not in nums[0:i]:
                #uniq.append(nums[i])
                nums[uniqcnt] = nums[i]
                uniqcnt += 1
        return uniqcnt   