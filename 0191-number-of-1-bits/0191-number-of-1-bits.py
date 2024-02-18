class Solution:
    def hammingWeight(self, n: int) -> int:
        # '1' bit 개수 세기
        count = 0
        for i in bin(n):
            if i=='1':
                count += 1 
        return count