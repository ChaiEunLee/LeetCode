class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # bin : 10진수->2진수로 바꾸는 함수
        # x^y 하면 알아서 2진수 XOR -> 10진수로 바꿔줌
        #print(x^y)
        #print(bin(x^y))
        return bin(x^y).count('1')