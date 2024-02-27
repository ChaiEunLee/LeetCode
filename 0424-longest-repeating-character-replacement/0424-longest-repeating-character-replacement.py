import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 오른쪽 포인터 위치 - 왼쪽 포인터 위치 => 윈도우 내 출현 빈도가 가장 높은 문자의 수 == k
        left = right = 0
        counts = collections.Counter()
        for right in range(1,len(s)+1): # string을 돌면서 
            #print(right)
            counts[s[right-1]] += 1 
            # most common char
            max_char_n = counts.most_common(1)[0][1] #most_common(1)=[('A':3)]: 최빈값 1개
            
            # k초과시 왼쪽 포인터 이동
            if right-left-max_char_n>k:
                counts[s[left]] -=1
                left+=1
            #print(right, left, max_char_n, s[left])
        return right-left