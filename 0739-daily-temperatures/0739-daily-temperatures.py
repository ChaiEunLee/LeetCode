class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 더 따뜻한 날까지 기다리는 기간. 끝은 무조건 0.
        # stack으로 쌓고 빼면서 기온 올라갔으면 빼고 아니면 놔두기.
        tempstack = []
        days = [0]*len(temperatures)
        # 날짜를 돌면서
        for i in range(len(temperatures)):
            # 오늘 기온이 더 높으면 계속 pop(). 
            while tempstack and temperatures[tempstack[-1]] < temperatures[i]:
                last = tempstack.pop()
                days[last] = i-last
            # 오늘 기온을 stack에 append
            tempstack.append(i)
            #print(i, temperatures[i], tempstack, days)
        
        return days