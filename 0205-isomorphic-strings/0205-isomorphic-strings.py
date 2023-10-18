class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # set이 같아야하고
        # 개수, 순서도..
        if len(set(s)) != len(set(t)):
            return False

        myDict = {}
        for i in range(len(s)):
            if s[i] in myDict:
                myDict[s[i]].append(i)
            else:
                myDict[s[i]] = [i]

        myDict2 = {}
        for j in range(len(t)):
            if t[j] in myDict2:
                myDict2[t[j]].append(j)
            else:
                myDict2[t[j]] = [j]
        
        for value in myDict.values():
            if value not in myDict2.values():
                return False

        return True