class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # collections.Counter(t) : t의 글자랑 개수를 세줌. 
        need, missing = collections.Counter(t), len(t)
        #print(need, missing)
        i = I = J = 0 # The current window is s[i:j] and the result window is s[I:J]
        
        for j, c in enumerate(s,1): #s글자 돌면서 
            missing -= need[c] > 0 #need에 있으면 missing-1
            need[c] -= 1 #need에서는 무조건 1 빼줌. 없는 단어면 -1이 들어감.
            if not missing: #missing>0
                # start index i 찾기
                while i<j and need[s[i]] < 0: #i<j인데 현재 단어가 필요없는 단어면 시작지점을 옮긴다. i+=1을 해줄것.
                    need[s[i]] += 1
                    i += 1
                # 끝까지 다 돌았거나, 이번에 돈게 J-I보다 작아서 짧은 길이가 발견되면 I,J 업데이트
                if not J or j-i <= J-I:
                    I,J = i,j
        return s[I:J]