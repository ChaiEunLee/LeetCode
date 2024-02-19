class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans<<1) + (n&1) 
            #n&1 맨 오른쪽bit가 1이면 1, 0이면 0이 나옴.
            # ans<<1 하고 + 위에서 구한 0/1을 오른쪽에 붙임. 
            n>>=1 # n 한칸 right shift해서 맨 오른쪽 자릿수 없앰. 
            #print(bin(n), bin(ans))
        return ans