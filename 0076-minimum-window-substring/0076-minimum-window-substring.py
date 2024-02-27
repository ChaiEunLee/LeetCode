import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t) #t element를 key, 개수를 value로 dict 만들어줌. 
        missing = len(t)
        left = start = end = 0
 
        # move right pointer
        for right, char in enumerate(s,1): # enumerate(s), index는 1부터
            print(right, char)
            missing -= need[char] > 0
            need[char] -= 1
            #print(missing, need)
            
            # move left pointer if missing is 0
            # 왼쪽 포인터를 더 줄여서 subarray를 더 줄일 수 있는지 확인
            if missing == 0:
                while left < right and need[s[left]] < 0: # need가 음수면 left pointer가 엉뚱한 글자를 가리키고 있을테니 0까지 이동하기.
                    need[s[left]] += 1
                    left += 1
                if not end or right-left <= end-start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
                    #print(need, missing, left)
                    
        return s[start:end]