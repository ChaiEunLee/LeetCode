class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(s_list) != len(pattern):
            return False
        
        myDict = {}
        
        for i in range(len(pattern)):
#            print(myDict, pattern[i], s_list[i])
            if pattern[i] in myDict:
                if myDict[pattern[i]] != s_list[i]:
#                    print('false')
                    return False
            else:
                if s_list[i] in myDict.values():
                    return False
                myDict[pattern[i]] = s_list[i]
                
        return True
    