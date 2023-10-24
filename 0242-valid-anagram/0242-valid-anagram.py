class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myDict = {}
        for i in range(len(s)):
            if s[i] in myDict:
                myDict[s[i]] += 1
            else:
                myDict[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] not in myDict:
                return False
            elif myDict[t[j]] == 0:
                return False
            else:
                myDict[t[j]] -= 1
        

        return True