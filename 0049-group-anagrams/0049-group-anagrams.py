class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for word in strs:
            sortword = ''.join(sorted(word)) #sorted(word)는 list, string을 sort하고 싶으면 이렇게 해야함.
            #print(sortword)
            if sortword not in myDict:
                myDict[sortword] = [word]
            else:
                myDict[sortword].append(word)
                
        return myDict.values()