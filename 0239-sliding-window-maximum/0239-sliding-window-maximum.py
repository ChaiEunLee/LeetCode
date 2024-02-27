import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        out = []
        for i,n in enumerate(nums):
            #print(i,n)
            while d and nums[d[-1]] < n:
                #print(d, nums[d[-1]])
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            if i>= k-1:
                out.append(nums[d[0]])
        return out