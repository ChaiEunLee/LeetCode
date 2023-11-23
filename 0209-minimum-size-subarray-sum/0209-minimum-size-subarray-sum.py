class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 시작지점을 정하고 한칸씩 이동하면서 값을 보고, 더 앞칸을 줄여가면서 짧은 array로 가는 방식
        
        i, res = 0, len(nums) + 1

        for j in range(len(nums)): # length
            target -= nums[j]
            print("j, target : ", j, ", ",target)
            while target <= 0: #target을 넘으면
                print("target<=0!")
                res = min(res, j-i+1) # res = min(전체길이+1, 이번 array 길이)
                target += nums[i] #시작지점을 더해줘서 한칸 이동
                i += 1 # 시작 지점 전진
                print("res, target, i: ", res, ", ", target, ", ", i)
            
        return res % (len(nums)+1) # 없으면 0 출력하려고