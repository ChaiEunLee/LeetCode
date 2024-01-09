import collections 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # pop(0) 대신 pop()을 사용한 stack으로 좀 더 효율적으로 구현
        graph = collections.defaultdict(list)
        
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        #print(graph)
        
        # stack에서 하나씩 꺼내서 route를 채우는 개념 
        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
            #print(route, stack)
        
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]