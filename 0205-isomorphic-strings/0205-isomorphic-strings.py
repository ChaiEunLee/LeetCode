class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # s="egg", t="add"일때,
        d = {}
        for i, j in zip(s, t): # e,a / g,d / g,d 
            if i not in d: #e가 key, a가 value로 들어갈건데,
                if j in d.values(): # 이미 e랑 매핑된 다른 알파벳이 있으면
                    return False # return False
                d[i] = j # 'e':'a'로 매핑

            else:
                if d[i] != j:
                    return False

        return True