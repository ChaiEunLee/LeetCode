class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {'(':')', '{':'}', '[':']'}
        queue = []
        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                queue.append(s[i])
            else:
                if queue:
                    tmp = queue.pop()
                else: 
                    return False
                if s[i] != myDict[tmp]:
                    return False
        # 괄호가 남아있으면
        if queue:
            return False
        return True
            