class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # base case
        if n==1: return [0]
        # adj 리스트를 만들어서 graph 형태로 만들어줌.
        adj = [set() for _ in range(n)]
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        # leaves를 만들어서 하나씩 제거할 예정
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        # 각 leave와 연결된 node를 제거, 그 node에 가서 leaves도 제거. - edge를 소거함.
        while n>2:
            n -= len(leaves) #leaves는 어차피 root가 될 수 없으니까 root 후보에서 제외
            newLeaves = []
            for i in leaves: 
                j = adj[i].pop() #j = 각 leave와 연결된 vertex
                adj[j].remove(i) # 그 leaves와 연결된 vertex에 가서 leaves를 제거
                if len(adj[j])==1:
                    newLeaves.append(j)
            leaves = newLeaves
        # 그러다가 edge가 1,2개 남으면 만나는 것.
        return leaves