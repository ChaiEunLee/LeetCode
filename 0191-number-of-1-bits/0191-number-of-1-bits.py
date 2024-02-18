class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            print(n, count)
            n &= n-1 # 1을 뺀 값과 AND 연산을 할 때마다 비트가 1씩 빠지게 됨. 0이 될 때까지 반복하면 1의 개수를 세게 됨.
            count += 1
        return count