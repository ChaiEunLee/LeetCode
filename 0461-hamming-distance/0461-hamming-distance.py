class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # bin : 10진수->2진수로 바꾸는 함수
        # x^y 하면 알아서 2진수 XOR -> 10진수로 바꿔줌
        xor = x^y
        count=0
        for _ in range(32):
#            print(xor, xor&1)
            count += xor & 1 #맨 뒷자리가 1인것만 count 하겠다는것(xor 결과가 1이면 다른거라서)
            xor = xor>>1 #shift
        return count