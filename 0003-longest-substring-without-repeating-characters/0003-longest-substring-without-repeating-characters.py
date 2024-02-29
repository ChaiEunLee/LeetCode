class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use set
        n = len(s)
        maxLength = 0
        charMap = {} #index를 넣기
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]]<left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right-left+1)
            else:
                left = charMap[s[right]]+1
                charMap[s[right]] = right
        return maxLength