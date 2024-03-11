class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # number of days you have to wait after the ith day to get warmer temperature
        # stack
        # 현재보다 기온이 올라가면 pop 아니면 놔두기?????그게 무슨말이지?
        
        # temperatures를 돌면서 
        # 오늘 기온보다 높아진 거 있으면 pop 후 오늘 기온 append
        
        tempstack = [0]
        days = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            #print(i, temperatures[tempstack])
            while tempstack and temperatures[tempstack[-1]] < temperatures[i]: #과거기온<현재기온
                # 현재기온보다 낮은 기온들을 넣어주는 방식
                last = tempstack.pop()
                days[last] = i-last
            tempstack.append(i)
            
        return days