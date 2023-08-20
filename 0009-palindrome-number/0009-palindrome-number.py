class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x>0 and x%10 == 0)):
            return False
        
        check = 0
        while(x>check):
            check = check*10 + x%10
            x = x//10

        if (x==check or x==check//10):
            return True
        else:
            return False