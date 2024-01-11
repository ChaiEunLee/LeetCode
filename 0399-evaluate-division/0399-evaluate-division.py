from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def answer(curr, value):
            #print(curr, value, self.seen, self.goal)
            
            # required: self.graph, self.goal, self.seen
            if curr == self.goal:
                return value
            
            # graph[a] = b, c라서 b,c하나씩 넣어보면서 값 비교하는 것
            for adj, adj_value in self.graph[curr].items():
                if adj not in self.seen: 
                    self.seen.add(adj) #각 b,c 를 self.seen에 추가 
                    result = answer(adj,value*adj_value) #answer(b, 1*2) a/b=2라서
                    if result != -1: #혹여나 안나오는 값이라 -1 return하면 끝내고
                        return result
                    # self.seen에서 b,c 제거. 다른 알파벳을 받아서 goal이랑 비교하려고 ??! 
                    self.seen.remove(adj)
            return -1
        
        self.graph = defaultdict(dict)
        self.seen = set() # all visited expressions
        
        for (a,b), value in zip(equations, values):
            self.graph[a][b] = value
            self.graph[b][a] = 1/value
            
        result = []
        for orig, self.goal in queries:
            #print("orig: ", orig, ", self.goal: ", self.goal)
            result.append(answer(orig,1) if orig in self.graph else -1)
            self.seen.clear()
            
        return result