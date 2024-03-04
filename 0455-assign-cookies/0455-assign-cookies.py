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
        i=j=0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
