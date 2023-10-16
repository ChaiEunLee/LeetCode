class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2): # need 3 numbers, so loop until len(nums)-2
            if i>0 and nums[i] == nums[i-1]: # i=i-1이면 i-1일때 이미 구했을테니 skip
                continue
                
            # Two pointers
            l,r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                
                if s<0:
                    l += 1
                elif s>0:
                    r -= 1
                else: #s==0
                    res.append([nums[i], nums[l], nums[r]])
                    # 다른 l,r을 만날때까지 이동
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    #새로운 l,r 지정
                    l += 1
                    r -= 1
        return res