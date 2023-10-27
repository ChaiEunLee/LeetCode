class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if nums[i-1] + 1 != nums[i] => end = nums[i-1] start = nums[i]
        answer = []
        
        if len(nums) >= 1:
            start = nums[0]
            
            for i in range(1,len(nums)):
                if nums[i-1]+1 != nums[i]:
                    end = nums[i-1]
                    if start == end:
                        answer.append(str(start))
                    else:
                        answer.append(str(start)+"->"+str(end))
                    start = nums[i]

            # last element
            end = nums[len(nums)-1]
            if start == end:
                answer.append(str(start))
            else:
                answer.append(str(start)+"->"+str(end))
            
        return answer