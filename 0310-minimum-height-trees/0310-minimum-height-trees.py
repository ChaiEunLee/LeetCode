import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 리프 노드를 하나씩 제거하면서 남아있는 값을 찾으면 가운데에 있는 노드이고 이걸 루트로 하면 최소 높이 구성이 가능함. 
        # 루트 찾기 -> 그걸로 트리 구성하기 
        
        if n<=1:
            return [0]
        
        # 양방향 graph 구성
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        # 연결된 노드가 하나면 그 노드는 leaf nodes
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # 1) 루프 노드 찾기                
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor])==1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            #print(leaves)
        return leaves