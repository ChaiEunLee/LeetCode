class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 그 값을 찾으면 left, right로 이동해서 찾기
        left,right = 0, len(nums)-1
        index = -1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                index=mid
                break
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        if index == -1:
            return [-1,-1]
        else:
            start, end = index,index
            while start>=0 and nums[start]==target:
                start -=1
            while end<len(nums) and nums[end]==target:
                end +=1
        return [start+1,end-1]