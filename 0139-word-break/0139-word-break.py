class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False]*len(s)
        # 단어의 끝 자리를 True로 두고, s의 마지막 글자가 True가 되면 꽉 채운거니까 맨 마지막 글자 return 
        for i in range(len(s)):
            #print(i)
            for word in wordDict:
                #print(word, i, len(word), i-len(word)+1, i+1, s[i-len(word)+1:i+1])
                # s의 index가 단어의 끝이되고 & dp에 값이 있거나 첫번째 단어이면 
                if word == s[i-len(word)+1:i+1] and (d[i-len(word)] or i-len(word)==-1):
                    d[i] = True
                    #print(d)
        return d[-1]