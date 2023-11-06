class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {'}':'{', ')':'(',']':'['}
        
        myStack = []
        for i in s:
            if i in ['(','[','{']:
                myStack.append(i)
            else:
                if not myStack:
                    return False
                tmp = myStack.pop()
                if tmp != myDict[i]:
                    return False                
        if myStack:
            return False
        return True