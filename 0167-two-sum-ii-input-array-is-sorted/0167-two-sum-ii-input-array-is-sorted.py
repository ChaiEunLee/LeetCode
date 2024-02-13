import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k,v in enumerate(numbers):
            expected = target-v
            nums = numbers[k+1:]
            i = bisect.bisect_left(nums, expected)
            if i<len(nums) and numbers[i+k+1]==expected:
                return k+1, i+k+2 #(기준인 k+1에다가 +i 더하는 위치인데, 정답은 index가 1부터 시작되므로 +1해줌)