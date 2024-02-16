class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # bin : 10진수->2진수로 바꾸는 함수
        # x^y 하면 알아서 2진수 XOR -> 10진수로 바꿔줌
        xor = x^y
        count=0
        while xor>0:
            #print(xor, xor-1, xor&(xor-1))
            xor &= (xor-1) #removes the last bit. 1을 카운트하는 방법인가봐??? 머리로는 이해안되지만 해보면 되긴함.
            count += 1
        return count