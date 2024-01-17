class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #for문 전체를 두번 돌면서
        
        def dfs(per):
            if len(per)==len(nums):
                answer.append(per)
                return 
            for k in range(len(nums)): 
                if nums[k] not in per:
                    dfs(per+[nums[k]])

        answer = []
        for i in range(len(nums)):
            dfs([nums[i]])
        return answer