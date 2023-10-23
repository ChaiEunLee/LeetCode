class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split(' ')
        #map은 list에 있는 글자를 숫자로 변환해줌
        print(list(map(pattern.find, pattern)))
        print(list(map(t.index, t)))
        
        return list(map(pattern.find, pattern)) == list(map(t.index, t))
        