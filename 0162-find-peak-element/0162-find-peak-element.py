class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peak element : an element that is strictly greater than its neighbors
        # O(logn)
        low, high = 0, len(nums)-1
        while low<high:
            mid1 = low+(high-low)//2
            mid2 = mid1+1
            if (nums[mid1]<nums[mid2]): #mid1<mid2니까 mid1은 답이 아니라서 mid2~high까지 보기
                low = mid2
            else: #mid1>mid2니까 mid1이 답일수도 있어서 low~mid1까지 보기
                high = mid1
        return low