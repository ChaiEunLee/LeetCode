class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2): # need 3 numbers, 그래서 len(nums)-2까지 range
            l, r = i+1, len(nums)-1 # l,r : 양 끝 pointer로 시작
            while l < r: # 
                sum = nums[i] + nums[l] + nums[r]
                
                # 찾으면 return
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum

                # 다른 숫자로 포인터 이동
                if sum < target: 
                    l += 1
                elif sum > target:
                    r -= 1
        return result        