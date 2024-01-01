class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 더 따뜻한 날까지 기다리는 기간. 끝은 무조건 0.
        # stack으로 쌓고 빼면서 기온 올라갔으면 빼고 아니면 놔두기.
        tempstack = []
        days = [0]*len(temperatures)
        for i, cur in enumerate(temperatures): #0부터 index, 각 값을 출력함.
            #print(i, cur)
            while tempstack and cur > temperatures[tempstack[-1]]:
                last = tempstack.pop()
                days[last] = i - last #매번 더하는게 아니라 나중에 차이를 계산해서 넣어주는 방식. 
            tempstack.append(i)
            #print(tempstack, days)
            
        return days