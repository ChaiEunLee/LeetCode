class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits)-1,-1,-1):
            number += digits[i] * (10**(len(digits)-i-1))
        answer = []
        number += 1
        
        while number > 0:
            answer = [number%10] + answer
            number = number // 10 
        return answer