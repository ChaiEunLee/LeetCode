class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer로 양쪽에서 오면서 짧은 기둥 기준으로 곱하기 -> 더 많으면 max area 덮어쓰기
        l = 0
        r = len(height)-1
        maxarea = 0
        
        while l<r:
#            maxarea = max(maxarea,min(height[r],height[l])*(r-l) )
            if maxarea < min(height[r],height[l])*(r-l):
                maxarea = min(height[r],height[l])*(r-l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea