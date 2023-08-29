class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s)-1
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        while(l<r):
            while(l<r and not s[l] in vowels):
                l += 1
            while(l<r and not s[r] in vowels):
                r -= 1
            # 'str' object does not support item assignment - 그래서 s를 list로 바꿔서 진행
            s[l], s[r] = s[r], s[l] 
            l += 1
            r -= 1
        return ''.join(s)