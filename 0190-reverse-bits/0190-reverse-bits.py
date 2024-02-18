class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bit = 31
        for i in range(len(bin(n))-1,1,-1): #n-1~2까지
            result += 2**(bit)*int(bin(n)[i])
            bit -= 1
            #print(i, result, bit)
        return result