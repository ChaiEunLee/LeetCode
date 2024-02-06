class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot 찾고 -> target 찾기
        if not nums:
            return -1
        
        # pivot 찾기
        left, right = 0, len(nums)-1
        while left< right:
            mid = left+(right-left)//2
            
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        pivot = left
                
        # pivot 기준 binary search
        left, right = 0, len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            mid_pivot = (mid+pivot)%len(nums) #pivot 앞/뒤의 mid를 구하기 위해서 +pivot을 하고 %len(nums)를 하는 것
#            print(left, right, mid_pivot)
            if nums[mid_pivot] < target:
                left = mid+1
            elif nums[mid_pivot] > target:
                right = mid-1
            else:
                return mid_pivot
            
        return -1