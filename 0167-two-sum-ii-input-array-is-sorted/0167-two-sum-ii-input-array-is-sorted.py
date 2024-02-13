import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k,v in enumerate(numbers):
            expected = target-v
            i = bisect.bisect_left(numbers, expected, k+1) # 내장된 bisect 파라미터 lo 사용
            if i<len(numbers) and numbers[i]==expected:
                return k+1, i+1