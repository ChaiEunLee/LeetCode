class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits #제일 왼쪽은 따로 더 있는 경우
        return [1] + digits #제일 왼쪽이 1인 경우