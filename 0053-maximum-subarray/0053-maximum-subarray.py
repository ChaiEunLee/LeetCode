class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Memoization
        sums = [nums[0]]
        #print("Start sums as ", sums)
        for i in range(1,len(nums)):
            #print("i: ", i)
            sums.append(nums[i]+ (sums[i-1] if sums[i-1]>0 else 0)) #sums[i-1]가 0보다 작으면 nums[i]로 새롭게 시작. 아니면 전꺼랑 합쳐서 누적 subarray구하기
            #print("result sums : ",sums)
        return max(sums)