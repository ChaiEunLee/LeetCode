class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda i: i[0]): #start 값 기준으로 정렬
            if out and i[0] <= out[-1][1]: #i[0](intervals start) <= out의 끝값의 end값 = 범위가 겹친다는 의미
                out[-1][1] = max(out[-1][1],i[1]) #out과 intervals end 값중에 큰걸로 값 대체. 
            else:
                out += [i]
         #   print(out)
        return out