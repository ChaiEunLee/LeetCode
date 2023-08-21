class Solution:
    def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf #종료. 절대 largest가 될 수 없는 값을 반환
            
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0 #init
            
            for i in range(mid-1, L-1, -1): # L: mid-1을 포함하는 subarray중에서 max subarray를 구함
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            
            cur_sum = 0
            for i in range(mid+1, R+1): # R: mid+1를 포함하는 subarray중에서 max subarray를 구함
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
                
            # L의 새로운 subarray, R의 새로운 subarray, mid를 포함하는 subarray 중 max
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum) 
        
        return maxSubArray(nums, 0, len(nums)-1)