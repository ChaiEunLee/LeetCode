class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time Complexity : O(n)
        myDict = {}
        for i in range(len(magazine)):
            if magazine[i] in myDict:
                myDict[magazine[i]] += 1
            else:
                myDict[magazine[i]] = 1
        
#        print(myDict)
        for j in range(len(ransomNote)):
            if ransomNote[j] in myDict and myDict[ransomNote[j]] > 0:
                myDict[ransomNote[j]] -= 1
            else:
                return False
#        print(myDict)
        return True
        