class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        start,end = 0, len(nums)-1
        
        while start<end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1 # +1 해줘야함
            else: #nums[mid] > target
                end = mid
            
        # 1 element left at the end
        return start+1 if nums[start] < target else start