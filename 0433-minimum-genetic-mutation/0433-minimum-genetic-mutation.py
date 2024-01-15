class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        q = deque([startGene])
        visited = {startGene} #set
        mutations = 0
        
        while q:    
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endGene:
                    return mutations
                for nei in bank:
                    if checkNeighbor(cur, nei) and nei not in visited:
                        visited.add(nei)
                        q.append(nei)      
            mutations += 1
        return -1