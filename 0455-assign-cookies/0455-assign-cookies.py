class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g,i) # g에서 cookie(=i)의 right index를 찾음. 작아서 없으면 0 출력.
            # children의 index인거니까 result보다 크면 쿠키를 줄 수 있다는 의미라서 result += 1. 어쩌면 result를 index 처럼 취급하는 걸지도.
            if index>result:
                result += 1
            #print(index, g, i, result)
        return result