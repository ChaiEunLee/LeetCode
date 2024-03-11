class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for loop 돌면서 현재 기온보다 낮은것들을 기록하기
        tempstack=[0] #index
        days = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            # tempstack 최근거부터 차근히. 날짜 세야해서
            while tempstack and temperatures[tempstack[-1]] < temperatures[i]:
                last = tempstack.pop()
                days[last] = i-last
            tempstack.append(i)
        return days