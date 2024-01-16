import collections
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for u,v,w in times:
            graph[u].append((v,w))
            
        # Q : [(소요시간, 현재노드까지의)]
        Q = [(0,k)]
        dist = collections.defaultdict(int)
        
        # Q 최소값 기준으로 정점까지 최단 경로 삽입
        # Heap : 작은 숫자부터 pop
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q,(alt,v)) #(time, node)
                   
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist)==n:
            return max(dist.values())
        return -1