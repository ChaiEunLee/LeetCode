class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n,x = -n, 1/x
        
        stack, ans = deque(), 1
        
        while n:
            n, bit = divmod(n,2) # share, remainder
            stack.append(bit) # append remainder
            
        while stack:
            bit = stack.pop() 
            ans *= ans # multiply share repeatedly
            if bit:
                ans *= x
                
        return ans