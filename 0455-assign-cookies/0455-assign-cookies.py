class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Can only give one cookie to each child
        # only if it is the same or bigger than each child's greed
        # return children number who can get cookie
        # O(n+m)
        result = 0
        g = sorted(g)
        s = sorted(s)
        #print(g)
        for i in range(len(g)):
            j = 0
            while j<len(s):
                if g[i]<=s[j]:
                    result += 1
                    s.remove(s[j])
                    #print(s)
                    break
                else:
                    j+=1
            #print(result, s)
        return result