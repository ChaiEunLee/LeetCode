import collections 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        # 그래프 순서대로 구성
        for a,b in sorted(tickets): # 알파벳 순서대로 sort
            graph[a].append(b)
#        print(graph)
        
        route = []
        def dfs(a):
            # 첫번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
#            print(a, route)
            
        dfs('JFK') 
        return route[::-1]