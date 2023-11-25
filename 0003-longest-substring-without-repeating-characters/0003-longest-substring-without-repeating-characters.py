class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # 해당 letter가 가장 최근에 몇번째에 나왔는지를 dictionary로 기록
        l = 0 # 시작지점
        output = 0 # 길이
        for r in range(len(s)):
#            print(s[r], seen, l, output)
            if s[r] not in seen:
                output = max(output, r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r-l+1) # r-l+1 = 현재위치-시작위치+1로 길이 측정
                else:
                    l = seen[s[r]] + 1 # 그 letter가 나왔던 그 위치 다음으로 시작 위치를 지정. 
            seen[s[r]] = r # seen[s[r]]을 현재 위치로 업데이트
        return output
                