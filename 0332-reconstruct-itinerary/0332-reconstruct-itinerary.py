import collections 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # pop(0) 대신 pop()을 사용한 stack으로 좀 더 효율적으로 구현
        graph = collections.defaultdict(list)
        
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        #print(graph)
        
        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            #print(a,route)
            
        dfs('JFK')
        # 다지 뒤집에서 어휘 순 결과로
        return route[::-1]
        