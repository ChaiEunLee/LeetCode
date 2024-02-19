class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            b = (b^n)&~a
            a = (a^n)&~b
        return b