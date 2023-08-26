class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort
        for i in range(len(nums)-2): # need 3 numbers, 그래서 len(nums)-2까지 range
            l,r = i+1, len(nums)-1 # i번째, i-1번째 숫자가 다르면 l,r two pointer 지정. l은 i+1 번째, r은 맨 오른쪽 끝으로 지정.
            if i==0 or nums[i] != nums[i-1]: # i번째, i-1번째 숫자가 같으면 아래 코드 skip    
                while l<r: # l,r 만나기 전까지
                    s = nums[i] + nums[l] + nums[r] # i번째 숫자 기준으로 합이 0이 되는 숫자 2개를 찾는 과정
                    if s<0: # 마이너스 숫자가 너무 크니까 
                        l += 1 # 오른쪽으로 이동
                    elif s>0: # 플러스 숫자가 너무 크니까 
                        r -= 1 # 왼쪽으로 이동
                    else: # s = 0
                        res.append((nums[i], nums[l], nums[r])) # 일치하는 숫자 찾으면 그거 넣어두고
                        
                        # 다른 숫자로 포인터 이동
                        while l<r and nums[l] == nums[l+1]: 
                            l += 1
                        while l<r and nums[l] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res