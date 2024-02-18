class Solution:
    def hammingWeight(self, n: int) -> int:
        # '1' bit 개수 세기
        count = 0
        while n>0:
            if n%2==1:
                count += 1
            n=n>>1
        return count