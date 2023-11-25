class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 길이를 1~len(s)/2로 늘려가면서 
        # 한칸씩 이동하면서 봐야하는데 
        sub = ""
        maxlength = 0
        for i in range(len(s)): #시작지점
            for j in range(i,len(s)): #시작지점부터 끝까지 돌면서
                if s[j] in sub: # repeating letter 나오면
                    sub = "" 
                    break     
                sub += s[j] # repeating letter 안 나올 때까지 더해주고 
                if maxlength < len(sub): # maxlength 업데이트
                    maxlength = len(sub)
                #print(sub, maxlength)
        return maxlength
            