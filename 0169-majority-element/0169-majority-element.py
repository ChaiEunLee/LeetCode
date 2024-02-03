import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 분할한 부분에서 과반을 찾아서 계속 위로 올려보내는 방식
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums)//2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        print([b,a])
        return [b,a][nums.count(a)>half]
        