import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #src->dst, at most k stops
        f = collections.defaultdict(dict) #dict in dict
        for a, b, p in flights:
            f[a][b] = p #{0:{1:100}, 1:...}
            
        heap = [(0, src, k+1)]
        seen_stops = collections.defaultdict(int)
        
        while heap:
            price, node, stop = heapq.heappop(heap)
            if node == dst:
                return price
            
            if stop < 0:
                continue
            if node in seen_stops and seen_stops[node] >= stop:
                continue
            seen_stops[node] = stop
            
            if stop > 0:
                for nextnode in f[node]:
                    heapq.heappush(heap, (price+f[node][nextnode], nextnode, stop-1))
        return -1