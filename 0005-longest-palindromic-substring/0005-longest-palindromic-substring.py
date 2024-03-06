class Solution:
    def longestPalindrome(self, s: str) -> str:
        #dp
        # state(start,end)==True인 것중 max(end-start+1)인걸 반환
        # startpoint + longest len 을 저장해서 마지막에 그 index로 찾아서 반환
        #when s[start]==s[end] & 'a': start==end, 'aa':start==end, 'aba':start+1==end-1, 'abba':start+1==end-1
        n=len(s)
        dp = [[False]*n for _ in range(n)] #multi dp[start][end]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome_start, longest_palindrome_len = 0,1
        #print(dp)
        
        for end in range(0,n): #end point 0~n
            for start in range(end-1,-1,-1): #end~start
                #print("end: ", end, ", start:", start, s[start], s[end])
                if s[start]==s[end]: #when s[start]==s[end]
                    if end-start==1 or dp[start+1][end-1]: #&한글자거나 start+1==end-1이면
                        dp[start][end] = True
                        palindrome_len = end-start+1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
                #print(dp)
        return s[longest_palindrome_start: longest_palindrome_start+longest_palindrome_len]
                        