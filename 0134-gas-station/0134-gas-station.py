class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별 
        if sum(gas)<sum(cost):
            return -1
        
        start, fuel = 0,0
        for i in range(len(gas)):
            #print(start, i, fuel)
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i+1
                fuel = 0
            else: #출발점이 되면 출발... 중간에 출발해도 len(gas)까지만 가면 되나?
                # 특정 부분에서 성립되지 않으면 그 앞은 전부 출발점이 될 수 없음.
                fuel += gas[i] - cost[i]
        return start